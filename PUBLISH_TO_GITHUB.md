# Publish the Public Showcase Safely

## Critical rule

Create the public repository from this clean showcase folder. Do not copy this
folder into the private engine's existing Git repository, and do not reuse a Git
history that ever contained the full notebook or source.

## PowerShell

```powershell
cd "$HOME\Downloads\obscura-public-showcase"

python scripts\audit_public_release.py .
pytest

git init
git add .
git commit -m "Initial OBSCURA public showcase"
git branch -M main

git remote add origin https://github.com/csalnav2/obscura-metamaterial-observability-lab.git
git push -u origin main
```

Using GitHub CLI:

```powershell
gh repo create obscura-metamaterial-observability-lab `
  --public `
  --source . `
  --remote origin `
  --push
```

## Bash

```bash
cd ~/Downloads/obscura-public-showcase

python scripts/audit_public_release.py .
pytest

git init
git add .
git commit -m "Initial OBSCURA public showcase"
git branch -M main

git remote add origin https://github.com/csalnav2/obscura-metamaterial-observability-lab.git
git push -u origin main
```

## Private core repository

Keep the complete notebook and source in a different private repository, such as
`obscura-core-private`. Before inviting a collaborator, establish the scope,
attribution, confidentiality, publication, and IP terms. Provide the smallest
module, dataset, executable, or interface that supports the collaboration.
