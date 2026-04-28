#!/bin/bash

set -e

echo "Initializing app"

echo "Downloading data from Azure"
python download_data.py

echo "Starting Streamlit"
exec python -m streamlit run app.py \
  --server.port=${PORT:-8000} \
  --server.address=0.0.0.0 \
  --server.headless=true