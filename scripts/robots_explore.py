#!/usr/bin/python3

####################################################
# Script per scaricare e analizzare il file robots.txt di un sito web
# Autore: Rocco <sheliak> Sicilia 
# Website: https://roccosicilia.com
####################################################

import sys
import requests

# verifico che sia stato passato un argomento
if len(sys.argv) != 2:
    print("Utilizzo: python script.py <URL>")
    sys.exit(1)

# costruisco l'URL completo
url = sys.argv[1].rstrip('/')
if not url.endswith('/robots.txt'):
    url += '/robots.txt'

try:
    # scarico il contenuto di robots.txt
    response = requests.get(url)
    content = response.text
except Exception as e:
    print(f"Errore nel download: {e}")
    sys.exit(1)

# estraggo e stampo i path
for line in content.splitlines():
    if line.startswith("Allow:") or line.startswith("Disallow:"):
        parts = line.split()
        if len(parts) == 2:
            print(parts[1])
