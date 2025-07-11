import json
import sys
import os

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file.json> <full|null>")
    sys.exit(1)

input_file = sys.argv[1]
full = sys.argv[2]

with open(input_file, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

oldhostlist = []
srvhostlist = []
fulllist = []

# print a list of interesting Windows hosts
print("\n##### Interesting Windows hosts:")
for entry in data.get("data", []):
    properties = entry.get("Properties", {})
    hostname = properties.get("name", "N/A")
    operatingsystem = properties.get("operatingsystem", "N/A")
    fulllist.append(hostname)
    if isinstance(operatingsystem, str) and ("2003" in operatingsystem or "2008" in operatingsystem or "XP" in operatingsystem or "Windows 7" in operatingsystem):
        print(f"Hostname: {hostname}, operatingsystem: {operatingsystem}")
        oldhostlist.append(hostname)

# check if the interesting host is online
print("\n##### Checking if hosts are online:")
for host in oldhostlist:
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    if response == 0:
        print(f"{host} is online with IP address {os.popen(f'getent hosts {host}').read().strip().split()[0]}")
    else:
        print(f"{host} is offline")

# print a list of Windows hosts with SMB shares
print("\n##### Windows hosts:")
for entry in data.get("data", []):
    properties = entry.get("Properties", {})
    hostname = properties.get("name", "N/A")
    operatingsystem = properties.get("operatingsystem", "N/A")
    fulllist.append(hostname)
    if isinstance(operatingsystem, str) and ("Server" in operatingsystem):
        print(f"Hostname: {hostname}, operatingsystem: {operatingsystem}")
        oldhostlist.append(hostname)

# check for any online hosts
if full == 'full':
    print("\n##### Checking for any online hosts:")
    for host in fulllist:
        response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
        if response == 0:
            print(f"{host} is online with IP address {os.popen(f'getent hosts {host}').read().strip().split()[0]}")
else:
    print("\n##### Skipping online check for hosts as 'full' is not specified.")
