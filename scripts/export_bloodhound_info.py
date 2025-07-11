import json
import sys
import os

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

    # print a list of interesting Windows hosts
    hostlist = []
    if isinstance(operatingsystem, str) and ("2003" in operatingsystem or "2008" in operatingsystem or "XP" in operatingsystem or "Windows 7" in operatingsystem):
        print(f"Hostname: {hostname}, operatingsystem: {operatingsystem}")
        hostlist.append(hostname)

    # check if the host is online
    for host in hostlist:
        response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
        if response == 0:
            print(f"{host} is online with IP address {os.popen(f'getent hosts {host}').read().strip().split()[0]}")
        else:
            print(f"{host} is offline")

    