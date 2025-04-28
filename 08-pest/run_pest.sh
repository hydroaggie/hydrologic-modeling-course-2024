#!/bin/bash
set -e  # Optional: exits on error, useful for debugging

python PFLOTRAN_pest.py
bash ppesttrial.sh
