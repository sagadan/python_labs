import json
from pathlib import Path

path = Path(r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/samples/people.json")
data = [{"name": "Liza", "age": 21}, {"name": "Maxim", "age": 22}]
with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with path.open(encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
import csv

rows = [
     {"city": "Khabarovsk", "okrug": "DVFO", "population": "615600","land area": "389"},
     {"city": "Ekaterinburg", "okrug": "UFO", "population": "1548187","land area": "1110"},
     {"city": "Novosibirsk", "okrug": "SFO", "population": "1637266","land area": "502.7"},
]
path = Path(r"/Users/elizavetazuzina/Documents/GitHub/python_labs/data/samples/city.csv")
with path.open("w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)