#!/bin/bash

cd "$(dirname "$0")"
python3 scraper.py
python3 -m csvtomd out.csv

