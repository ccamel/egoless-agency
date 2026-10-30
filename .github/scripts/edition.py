#!/usr/bin/env python3
import sys
from pathlib import Path


def roman(number):
    if number < 1:
        raise ValueError("💀 edition number must be positive")
    result = []
    for value, symbol in (
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
    ):
        count, number = divmod(number, value)
        result.append(symbol * count)
    return "".join(result)


def render(html, number):
    marker = "<!-- edition -->"
    if html.count(marker) != 1:
        raise ValueError("💀 expected exactly one edition marker")
    return html.replace(marker, f'<span class="edition">edition {roman(number)}</span>')


if __name__ == "__main__":
    number = int(sys.argv[1])
    path = Path(sys.argv[2])
    path.write_text(render(path.read_text(encoding="utf-8"), number), encoding="utf-8")
    print(roman(number))
