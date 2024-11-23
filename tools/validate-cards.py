import argparse

import numbers_parser  # type: ignore[import-untyped]

from ship_it_tools import counts, meta


def _read_card_counts(cards_path: str) -> list[int]:
    document = numbers_parser.Document(cards_path)

    card_counts = []
    for card_sheet in document.sheets:
        if card_sheet.name.endswith(meta.COPY_MARKER):
            continue

        cell_value = card_sheet.tables[0].cell("E18").value.strip()
        if cell_value.startswith("="):  # `= number of players`
            card_counts.append(meta.NUMBER_OF_PLAYERS)
        else:
            card_counts.append(int(cell_value.strip().split(" ")[0]))
    return card_counts


def _validate(cards_path: str, counts: list[int]) -> None:
    card_counts = _read_card_counts(cards_path)
    if card_counts != counts:
        raise ValueError(
            "Not equal", card_counts, len(card_counts), counts, len(counts)
        )


def main() -> None:
    """Run the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "cards",
        type=str,  # TODO: use `filepath` type
        help="Path to `cards.numbers` file with cards definitions",
    )
    parser.add_argument(
        "counts",
        type=str,  # TODO: use `filepath` type
        help="Path to `counts.numbers` file with card counts",
    )
    parsed_args = parser.parse_args()
    _validate(
        parsed_args.cards,
        counts.read_counts(parsed_args.counts, squash_copies=True),
    )


if __name__ == "__main__":
    main()
