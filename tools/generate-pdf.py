"""
Creates PDF to be printed from the inputs: cards' pdf and their counts.

Basically it reads the input pdf with cards design
and their counts from `counts.numbers`.

Right now it is impossible to export PDFs from `cards.numbers` as far as I know.
To export them:
1. Open `cards.numbers`
2. Click `Export as`
3. Select `PDF`
4. Set the best quality
5. Select "page view" as size
6. Done!
"""

# TODO: also provide validation, that `counts.numbers`
# has the same count as right-bottom card corner
# TODO: validate the order of counts and cards by name?

import argparse
import contextlib
import io
import os

import pypdfium2 as pdf  # type: ignore[import-untyped]
from ship_it_tools import counts


def _write_cards_with_counts(
    cards: io.BytesIO,
    counts: list[int],
    output_file: str,
) -> None:
    _validate_counts()
    dest_pdf = pdf.PdfDocument.new()
    src_pdf = pdf.PdfDocument(cards)

    with contextlib.closing(src_pdf), contextlib.closing(dest_pdf):
        for page_index, count in enumerate(counts):
            for _ in range(count):
                dest_pdf.import_pages(src_pdf, [page_index])

        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        with open(output_file, mode="wb") as output:
            dest_pdf.save(output)


def main() -> None:
    """Run the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cards",
        type=argparse.FileType(mode="rb"),
        help="Path to original cards PDF file exported from `cards.numbers`",
    )
    parser.add_argument(
        "counts",
        type=str,  # TODO: use `filepath` type
        help="Path to `counts.numbers` file with card counts",
    )
    parser.add_argument(
        "--output-file",
        type=str,  # TODO: dirname
        help="output location",
        required=True,
    )
    parsed_args = parser.parse_args()
    _write_cards_with_counts(
        parsed_args.cards,
        counts.read_counts(parsed_args.counts),
        parsed_args.output_file,
    )


if __name__ == "__main__":
    main()
