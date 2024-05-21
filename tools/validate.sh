#!/usr/bin/env bash

set -e

# Check if card counts are identical in `counts.numbers` and `cards.numbers`:
python tools/validate-cards.py ru/cards.numbers ru/counts.numbers
