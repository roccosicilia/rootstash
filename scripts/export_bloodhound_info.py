import json
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <input_file.json>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

for entry in data.get("data", []):
    properties = entry.get("Properties", {})
    hostname = properties.get("name", "N/A")
    operatingsystem = properties.get("operatingsystem", "N/A")
    if isinstance(operatingsystem, str) and ("2003" in operatingsystem or "2008" in operatingsystem):
        print(f"Hostname: {hostname}, operatingsystem: {operatingsystem}")