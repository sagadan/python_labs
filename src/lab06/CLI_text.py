import sys, os
import argparse
from pathlib import Path
from src.lib.text_stats import stats_text

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lib.io_txt_csv import read_text


def check_file(file_path: str) -> bool:
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не существует", file=sys.stderr)
        return False
    if not os.path.isfile(file_path):
        print(f"Ошибка: '{file_path}' не является файлом", file=sys.stderr)
        return False

    return True


def cat_command(input_file: str, number_lines: bool = False):
    if not check_file(input_file):
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                if number_lines:
                    print(f"{line_number:6d}  {line}", end='')
                else:
                    print(line, end='')
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)


def stats_command(input_file: str, top_n: int = 5):
    if not check_file(input_file):
        sys.exit(1)

    if top_n <= 0:
        print("Ошибка: значение --top должно быть положительным числом", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
            stats_text(text, top_n)

    except Exception as e:
        print(f"Ошибка при анализе файла: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        if not check_file(args.input):
            sys.exit(1)

        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                if args.n:
                    for line_number, line in enumerate(f, start=1):
                        print(f"{line_number:6d}  {line}", end='')
                else:
                    for line in f:
                        print(line, end='')
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "stats":
        if not check_file(args.input):
            sys.exit(1)

        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
                for e in top_n(count_freq(tokenize(normalize(text))), args.top):
                    print(e[0], e[1])
        except Exception as e:
            print(f"Ошибка при анализе файла: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()


"  python3 -m src.lab06.CLI_text cat --input data/samples/people.csv -n   "
"  python3 -m src.lab06.CLI_text stats --input  data/samples/people.csv --top 5   "
"  python3 -m src.lab06.CLI_text --help  "