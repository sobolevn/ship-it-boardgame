import argparse
import io
import os

import pypdfium2 as pdf


def _render_images(cards: io.BytesIO, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    src_pdf = pdf.PdfDocument(cards)
    for page_index, page in enumerate(src_pdf):
        page.render().to_pil().save(
            os.path.join(output_dir, f'{page_index}.jpg'),
        )


def main() -> None:
    """Run the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cards',
        type=argparse.FileType(mode='rb'),
        help='pdf with all the cards',
    )
    parser.add_argument(
        '--output-dir',
        type=str,  # TODO: dirname
        help='output location',
        required=True,
    )
    parsed_args = parser.parse_args()
    _render_images(parsed_args.cards, parsed_args.output_dir)


if __name__ == '__main__':
    main()
