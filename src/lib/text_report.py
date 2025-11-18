import os, csv, sys
from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab03.text_stats import table

if not os.path.exists(r"/data/lab_4/4.txt"):
    print(f"Ошибка: входной файл '{'4.txt'}' не найден.")
    sys.exit(1)

try:
    with open(r"/data/lab_4/4.txt", "r", encoding="utf-8") as f:
        text = f.read()
except UnicodeDecodeError:
    print(f"Ошибка: не удалось прочитать файл с кодировкой. Попробуйте encoding cp65001")
    sys.exit(1)

words = tokenize(normalize(text))

total_words = len(words)
freqs = count_freq(words)
unique_words = len(freqs)
sorted_words = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))
output_dir = r"/data"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "report.csv")
with open(output_path, "w", encoding="cp65001", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["word", "count"])
    for word, count in sorted_words:
        writer.writerow([word, count])

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")

top_5 = top_n(freqs, 5)
print("Топ-5:")
print(table(top_5, True))