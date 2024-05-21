#!/usr/bin/env bash

set -e

if [[ -z "$1" ]]; then
  echo 'usage: build.sh cards_pdf'
  echo 'cards_pdf argument is missing'
  exit 1
fi

set -x

# Clean existing build:
rm -rf build

# Run validation:
source tools/validate.sh

# Just all cards types in one pdf:
CARDS_PDF="$1"
# All cards in one pdf, with correct counts, useful for printing:
CARDS_WITH_COUNTS_PDF='build/cards-with-counts.pdf'

# Copy things:
mkdir -p build/covers
cp ru/graphics/cover_dark.png build/covers
cp ru/graphics/cover_white.png build/covers

python tools/generate-pdf.py "$CARDS_PDF" ru/counts.numbers \
  --output-file "$CARDS_WITH_COUNTS_PDF"

# Generate images for TG stickers and stuff:
python tools/generate-images-from-pdf.py "$CARDS_PDF" \
  --output-dir build/images

# Table Top Simulator:
python tools/generate-images-from-pdf.py "$CARDS_WITH_COUNTS_PDF" \
  --output-dir build/images-counts

# Generate TTS json:
python tools/tts-exporter.py build/images-counts
