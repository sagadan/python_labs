import sys

sys.path.append("/Users/elizavetazuzina/Documents/GitHub/python_labs/src/lib")
from A import normalize, tokenize, count_freq, top_n


def main():
    a = tokenize(normalize(sys.stdin.read()))
    print(f"Всего слов: {len(a)}")
    print(f"Уникальных слов: {len(set(a))}")
    print("Топ-5")
    # for e in top_n(count_freq(a)):
    #     print(f'{e[0]}: {e[1]}')
    for e in top_n(count_freq(a)):
        print(f"{e[0]}: {e[1]}")


if __name__ == "__main__":
    main()

# echo 'Привет, мир! Привет!!!' | python src/lab03/B.py
