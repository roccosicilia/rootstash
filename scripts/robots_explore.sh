#!/bin/bash

####################################################
# Script per scaricare e analizzare il file robots.txt di un sito web
# Autore: Rocco <sheliak> Sicilia
# Website: https://roccosicilia.com
####################################################

# verifica presenza argomento (URL)
if [ -z "$1" ]; then
    echo "Utilizzo: $0 <URL>"
    exit 1
fi

# definisce URL completa
URL="$1"
if [[ "$URL" != */robots.txt ]]; then
    URL="${URL%/}/robots.txt"
fi

# filtro path
curl -s "$URL" | grep "Allow" | awk '{print $2}'
curl -s "$URL" | grep "Disallow" | awk '{print $2}'
