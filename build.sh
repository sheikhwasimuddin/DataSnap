#!/usr/bin/env bash
set -o errexit

# Use python -m pip to guarantee we install into the active venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Force setuptools into the venv AFTER other deps (pip may skip it otherwise)
python -m pip install --ignore-installed setuptools

# Verify pkg_resources is importable
python -c "import pkg_resources; print('pkg_resources OK')"
