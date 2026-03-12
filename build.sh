#!/usr/bin/env bash
set -o errexit

# Force-install setuptools into the venv — required by gcloud (pyrebase4 dependency)
# Without --force-reinstall, pip may skip it if satisfied by system Python
pip install --force-reinstall setuptools wheel
pip install -r requirements.txt
