#!/usr/bin/env bash
set -o errexit

# Install setuptools first — required by gcloud (pyrebase4 dependency)
pip install setuptools wheel
pip install -r requirements.txt
