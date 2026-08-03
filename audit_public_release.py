#!/usr/bin/env python3
"""Fail closed when a public OBSCURA tree appears to contain private material."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Iterable

PRIVATE_SOURCE_SHA256 = "fd590af7c2d141d9749f92b6d7d1a37bea8a02681b397a827481e4347b68c3b8"
PRIVATE_NOTEBOOK_SHA256 = "dcf329f398b73499594ebfd89acc7f36249043ec46f494d738b5f9d4df56c6a0"
MAX_PUBLIC_TEXT_BYTES = 1_500_000
MAX_NOTEBOOK_CODE_CELL_CHARS = 50_000

# These implementation identifiers belong in the private repository only.
# They are deliberately assembled rather than written as contiguous literals so
# this audit file cannot trigger itself if it is accidentally included in a scan.
FORBIDDEN_CODE_IDENTIFIERS = tuple(
    "".join(parts)
    for parts in (
        ("anisotropic_", "permittivity_evaluation"),
        ("material_", "response"),
        ("objective_", "components"),
        ("spectral_", "objective_components"),
        ("class ", "SPSA", "Controller"),
        ("class ", "Live", "Simulation"),
        ("quantum_density_matrix_", "numpy_from_params"),
        ("illumination_", "stress_schedule"),
        ("msga_qfi_", "recovery_components"),
        ("%%writefile ", "u.py"),
    )
)

SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?:ghp|github_pat)_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)ngrok[_ -]?authtoken\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?i)openai[_ -]?api[_ -]?key\s*[:=]\s*['\"]?[^\s'\"]{16,}"),
    re.compile(r"https://[^\s]+\.ngrok[^\s?]*\?access=[A-Za-z0-9_-]{12,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)

TEXT_EXTENSIONS = {
    ".py", ".ipynb", ".md", ".txt", ".toml", ".yml", ".yaml", ".json",
    ".csv", ".html", ".css", ".js", ".cff", ".gitignore", ".gitattributes",
}
CODE_EXTENSIONS = {".py", ".ipynb", ".js"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in {"LICENSE", "NOTICE", ".gitignore", ".gitattributes"}


def audit_notebook(path: Path, findings: list[str]) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        findings.append(f"{path}: invalid notebook JSON: {exc}")
        return
    for index, cell in enumerate(notebook.get("cells", [])):
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code" and len(source) > MAX_NOTEBOOK_CODE_CELL_CHARS:
            findings.append(
                f"{path}: code cell {index} is {len(source):,} characters; public limit is {MAX_NOTEBOOK_CODE_CELL_CHARS:,}"
            )
        output_text = json.dumps(cell.get("outputs", []), ensure_ascii=False)
        for pattern in SECRET_PATTERNS:
            if pattern.search(source) or pattern.search(output_text):
                findings.append(f"{path}: possible secret or access URL in cell {index}")
        for identifier in FORBIDDEN_CODE_IDENTIFIERS:
            if identifier in source:
                findings.append(f"{path}: private implementation identifier {identifier!r} in cell {index}")


def audit_tree(root: Path) -> list[str]:
    root = root.resolve()
    findings: list[str] = []
    self_path = Path(__file__).resolve()
    for path in iter_files(root):
        if path.resolve() == self_path:
            continue
        digest = sha256(path)
        if digest in {PRIVATE_SOURCE_SHA256, PRIVATE_NOTEBOOK_SHA256}:
            findings.append(f"{path}: exact private artifact hash detected")
        if path.suffix.lower() == ".ipynb":
            audit_notebook(path, findings)
        if not is_text_candidate(path):
            continue
        if path.stat().st_size > MAX_PUBLIC_TEXT_BYTES and path.suffix.lower() not in {".html"}:
            findings.append(f"{path}: unusually large public text file ({path.stat().st_size:,} bytes)")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(f"{path}: possible credential, private key, or magic access URL")
                break
        if path.suffix.lower() in CODE_EXTENSIONS:
            for identifier in FORBIDDEN_CODE_IDENTIFIERS:
                if identifier in text:
                    findings.append(f"{path}: private implementation identifier {identifier!r}")
    return sorted(set(findings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    findings = audit_tree(args.root)
    if findings:
        print("PUBLIC RELEASE AUDIT: FAIL", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        return 1
    print("PUBLIC RELEASE AUDIT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
