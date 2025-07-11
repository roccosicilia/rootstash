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
    for ace in entry.get("Aces", []):
        print(f"Hostname: {hostname}, PrincipalSID: {ace.get('PrincipalSID')}, RightName: {ace.get('RightName')}")