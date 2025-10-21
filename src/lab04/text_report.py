from io_txt_csv import read_text, write_csv, ensure_parent_dir
import sys
from pathlib import Path
import os

from src.lib0 import normalize

sys.path.append(f'/Users/elizavetazuzina/Documents/GitHub/python_labs/src/lib')
from src.lib import text as text

from text import *
def exist_path(path_f: str):
    return os.path.exists(path_f)


def main(file: str, encoding: str = 'utf-8'):
    if not exist_path(file):
        raise FileExistsError('Файла не существует')

    text = read_text(file, encoding=encoding)
    norm = normalize(text)
    tokens = tokenize(norm)
    top = top_n(count_freq(tokens), 5)

    top_sort = sorted(top, key=lambda x: (x[1], x[0]))
    output_path = Path(file).parent / 'report.csv'
    write_csv(top_sort, str(output_path), header=('word', 'count'))

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(count_freq(tokens))}')
    print('Топ-5:')
    for word, count in top_sort:
        print(f'{word}: {count}')



path = r'/Users/elizavetazuzina/Documents/GitHub/python_labs/src/data'
main(path + r'/Users/elizavetazuzina/Documents/GitHub/python_labs/data/input.txt')
