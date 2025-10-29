import csv, json, sys, os


def is_valid_json_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return isinstance(json_data, list) and len(json_data) > 0 and all(
                isinstance(item, dict) for item in json_data)
    except:
        return False


def is_valid_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            return header is not None and len(header) > 0
    except:
        return False


def json_to_csv(json_path: str, csv_path: str) -> None:
    if not is_valid_json_file(json_path):
        print("ValueError: Input file is not a valid JSON or is empty")
        sys.exit(1)

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    if not is_valid_csv_file(csv_path):
        print("ValueError: Input file is not a valid CSV or is empty")
        sys.exit(1)

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


csv_to_json(r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/samples/people.csv",
            r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/out/people_from_csv.json")

json_to_csv(r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/samples/people.json", r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/out/people_from_json.csv")