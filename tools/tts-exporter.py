"""
Script to export cards to Table Top Simulator.

Read more:
https://www.makeuseof.com/how-to-make-custom-board-game-tabletop-simulator/

To export cards to Table Top Simulator:
1. Generate `cards-with-counts.pdf` using `generate-pdf.py`
# TODO
"""

import argparse
import os
from pathlib import Path

from PIL import Image

TTS_WIDTH = 10
TTS_HEIGHT = 7
TTS_FORMAT = TTS_WIDTH * TTS_HEIGHT
TTS_MAX_SIZE = 10000
NUM_OF_ARCH_CARDS = 5


def _count_files(image_dir: str) -> int:
    files = 0
    for filename in Path(os.curdir, image_dir).iterdir():
        if filename.is_file():
            files += 1
    return files


def _create_filename(
    filename: int,
    image_dir: str,
    files_count: int,
    *,
    is_back: bool,
) -> str:
    if is_back:
        if filename >= files_count:
            raise FileNotFoundError
        cover_dir = os.path.join(
            os.path.dirname(image_dir),
            'covers',
        )
        if filename >= NUM_OF_ARCH_CARDS:
            return os.path.join(cover_dir, 'cover_dark.png')
        return os.path.join(cover_dir, 'cover_white.png')
    return os.path.join(image_dir, f'{filename}.jpg')


def _create_sheet(
    sheet: int,
    image_dir: str,
    files_count: int,
    *,
    is_back: bool = False,
) -> None:
    dest_image = None
    for image in range(TTS_FORMAT * (sheet + 1)):
        filename = image + TTS_FORMAT * sheet
        try:
            current_image = Image.open(_create_filename(
                filename,
                image_dir,
                files_count,
                is_back=is_back,
            ))
        except FileNotFoundError:
            break
        if dest_image is None:
            dest_image = Image.new('RGB', (
                current_image.width * TTS_WIDTH,
                current_image.height * TTS_HEIGHT,
            ))
        dest_image.paste(current_image, (
            current_image.width * (image % TTS_WIDTH),
            current_image.height * (image // TTS_WIDTH),
        ))
        current_image.close()

    # Resize to be 10k pixels max:
    wpercent = (TTS_MAX_SIZE / dest_image.size[0])
    hsize = int(dest_image.size[1] * wpercent)
    filename_suffix = 'back' if is_back else 'front'
    dest_image.resize(
        (TTS_MAX_SIZE, hsize),
        Image.Resampling.LANCZOS,
    ).save(os.path.join('build', 'tts', f'{sheet}-{filename_suffix}.jpg'))
    dest_image.close()


def _create_tts_images(image_dir: str) -> None:
    output_dir = os.path.join('build', 'tts')
    os.makedirs(output_dir, exist_ok=True)

    files_count = _count_files(image_dir)
    for sheet in range(files_count // TTS_FORMAT + 1):
        _create_sheet(sheet, image_dir, files_count)
    for sheet in range(files_count // TTS_FORMAT + 1):
        _create_sheet(sheet, image_dir, files_count, is_back=True)


def main() -> None:
    """Run the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'images_dir',
        type=str,  # TODO: dirname
        help='Folder with all card types images',
    )
    # parser.add_argument(
    #     '--local-build',
    #     action='store_true',
    #     help='Set to toggle a local build for local TTS game only',
    # )
    parsed_args = parser.parse_args()
    _create_tts_images(parsed_args.images_dir)


if __name__ == '__main__':
    main()
