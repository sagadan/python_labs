import csv, os
from pathlib import Path

def read_text(path: str, encoding: str = "utf-8"):
    try:
        with open(path , encoding=encoding) as file:
            text = file.read()
            return text
    except UnicodeDecodeError:
        print("Неверная кодировка данных")
    except FileNotFoundError:
        print("Файл не найден, укажите полный путь к файлу")

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
        with open(path, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if header is not None:
                writer.writerow(header)
            lenr = len(rows[0])
            for row in rows:
                if len(row) != lenr:
                    print("ValueError")
            writer.writerows(rows)


def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Директория создана или уже существует: {directory_path}")
        return True
    except Exception as e:
        print(f"Ошибка при создании директории: {e}")
        return False
