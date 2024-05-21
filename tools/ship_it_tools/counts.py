import numbers_parser  # type: ignore[import-untyped]


def read_counts(counts_path: str) -> list[int]:
    """Return the list of ints of cards' counts definned in `counts.numbers`."""
    document = numbers_parser.Document(counts_path)
    table = document.sheets[0].tables[0]

    read_counts = []
    for row in range(table.num_rows):
        cell = table.cell(f"C{row + 1}").value
        if cell:
            read_counts.append(int(cell))
    return read_counts
