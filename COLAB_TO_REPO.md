# Moving the full Google Colab notebook into the repository

The repository is usable before the original notebook arrives. `obscura.py` is the authoritative scientific source, while the included launcher notebook provides a clean Colab entry point.

## When the full notebook is available

1. Download it from Colab as `.ipynb`.
2. Rename it to `OBSCURA_full_research_notebook.ipynb`.
3. Place it in `notebooks/`.
4. Remove all API keys, ngrok tokens, magic links, cookies, and private URLs.
5. Clear large cell outputs unless they are essential evidence.
6. Replace duplicated monolithic source cells with a command that runs `u.py`, or clearly label the notebook copy as generated.
7. Run the scanner:

   ```bash
   python scripts/validate_notebook.py notebooks/OBSCURA_full_research_notebook.ipynb
   ```

8. Run the notebook top to bottom in a fresh runtime.
9. Save the exact dependency versions and media manifest.
10. Commit a small preview image, not the complete generated media cache.

## Recommended notebook architecture

1. Project scope and claim boundary.
2. Dependency installation.
3. Secret loading through Colab Secrets.
4. Repository validation.
5. Deterministic self-test.
6. Fast smoke render.
7. Production precompute and dashboard launch.
8. Export collection and hash report.
9. Result interpretation checklist.

## Do not commit

- `.env`
- API keys or ngrok tokens
- Dashboard magic-link URLs
- `.dual_visibility_media/`
- Multi-gigabyte MP4/GIF caches
- Raw voice recordings
- Browser session data
