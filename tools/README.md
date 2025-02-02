# Tools for Ship IT!

## Installing dependencies

macOS:

```bash
brew install snappy
CPPFLAGS='-I/opt/homebrew/include -L/opt/homebrew/lib' poetry install
```

Linux:

```bash
sudo apt-get -y install libsnappy-dev
poetry install
```

For Windows you can follow: https://pypi.org/project/numbers-parser/

## Making a release

1. First, export `cards.pdf` from `cards.numbers`, [see this doc](https://github.com/sobolevn/ship-it-boardgame/blob/master/tools/generate-pdf.py)
2. Run `bash tools/build.sh "$PATH_TO_CARDS_PDF"`

Copy the last version description from `CHANGELOG.md`
to the version release page
and attach `build/cards-with-counts.pdf` as well.
