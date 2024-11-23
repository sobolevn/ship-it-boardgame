import numbers_parser  # type: ignore[import-untyped]

from ship_it_tools import meta


def read_counts(
    counts_path: str,
    *,
    squash_copies: bool = False,
) -> list[int]:
    """Return the list of ints of cards' counts definned in `counts.numbers`."""
    document = numbers_parser.Document(counts_path)
    table = document.sheets[0].tables[0]

    read_counts = []
    for row in range(table.num_rows):
        cell = table.cell(f"C{row + 1}").value
        if not cell:
            continue

        if squash_copies:
            name_cell = table.cell(f"B{row + 1}").value
            if (
                name_cell
                and isinstance(name_cell, str)
                and name_cell.strip().endswith(meta.COPY_MARKER)
            ):
                assert read_counts, f"{name_cell!r} does not have original"
                read_counts[-1] += int(cell)
                continue

        read_counts.append(int(cell))
    return read_counts
