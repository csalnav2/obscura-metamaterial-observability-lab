# Validation status for this GitHub packaging pass

Date: 2026-08-02

## Completed here

- Preserved the uploaded v16.45 Python source byte-for-byte as `obscura.py`.
- Verified SHA-256: `fd590af7c2d141d9749f92b6d7d1a37bea8a02681b397a827481e4347b68c3b8`.
- Verified line count: `56,783`.
- Ran `python -m py_compile` successfully on the uploaded source.
- Parsed the complete source with the Python AST.
- Verified the expected active figure-builder inventory.
- Verified the 11 mounted graph IDs are represented in the source.
- Added a compatibility `u.py` launcher without modifying the scientific implementation.
- Added repository-only tests that avoid importing the WSGI side-effect path.
- Added a no-secret notebook scanner and a minimal Colab launcher notebook.

## Not completed in this packaging environment

The packaging environment did not contain all dashboard runtime dependencies. In particular, Dash, Flask, Werkzeug, pyngrok, and QuTiP were unavailable. Therefore the following were not claimed as completed here:

- `python -u u.py --self-test`
- Full dashboard launch
- Full media precompute
- FFmpeg production render at 2560 by 1440 and 40 fps
- ngrok tunnel creation
- QuTiP parity test
- Browser callback and Realtime voice testing

## Required next validation in Colab or a clean local environment

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-optional.txt
python scripts/validate_repo.py
python -m pytest
python -u u.py --self-test
python -u u.py --verify-quantum-backends --compute-backend jax --qfi-derivative autodiff
```

Then perform one small launch before the production render:

```bash
python -u u.py \
  --render-only \
  --precompute-media \
  --media-seconds 3 \
  --media-fps 12 \
  --media-width 960 \
  --media-height 540 \
  --ffmpeg-exe /usr/bin/ffmpeg
```

Archive the command, environment lock, seed, manifest, raw CSV/JSON/NPZ exports, and SHA-256 hashes with any public result.
