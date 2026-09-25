"""TOML serialization helpers for pyproject writers."""

import tomlkit
from tomlkit.items import Whitespace


def ensure_trailing_blank_line(table) -> None:
    """Leave a blank line after a nested TOML table.

    tomlkit writes a newly created table immediately against the next
    sibling header. Drop any existing trailing whitespace items and
    append one newline so the following section stays separated.
    """
    body = getattr(getattr(table, "value", None), "body", None)
    if body is None:
        return
    while body and isinstance(body[-1][1], Whitespace):
        body.pop()
    table.add(tomlkit.nl())
