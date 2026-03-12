#!/usr/bin/env bash
set -o errexit

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Verify pkg_resources is importable (gcloud requires it)
python -c "import pkg_resources; print('pkg_resources OK')"
