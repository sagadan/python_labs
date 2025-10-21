from pathlib import Path
import csv
import os
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    with p.open('w', newline="", encoding="utf-8") as file:
        file_c = csv.writer(file)
        if header is None and rows == []:
            file_c.writerow(('a', 'b'))
        if header is not None:
            file_c.writerow(header)
        if rows != []:
            const = len(rows[0])
            for i in rows:
                if len(i) != const:
                    return ValueError
        file_c.writerows(rows)


def ensure_parent_dir(path: str | Path) -> None:
    path = os.path.dirname(path)
    Path(path).mkdir(parents=True, exist_ok=True)


print(read_text(r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/input.txt"))
write_csv([("word","count"),("test",3)], r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/check.csv")

