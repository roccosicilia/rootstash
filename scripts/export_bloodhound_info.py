import json
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_file.json>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

for element in data.get("Aces", []):
    print(f"Hostname: {element['name']}, RightName: {element['RightName']}")