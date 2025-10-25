# Discovery

Bash Script per discovery ICMP di una rete:
''' bash
#!/bin/bash

# controllo argomento "rete"
if [ -z "$1" ]; then
    echo "Uso: $0 <rete>"
    echo "Esempio: $0 192.168.1"
    exit 1
fi

NETWORK=$1

echo "Scansione della rete ${NETWORK}.0/24..."
echo ""

# ping intervallo 1-254
for i in {1..254}; do
    ping -c 1 -W 1 ${NETWORK}.$i > /dev/null 2>&1 && echo "${NETWORK}.$i" >> ${NETWORK}.iplist &
done
wait

echo ""
echo "Scansione completata"
'''

Scansione via NC sull'output della discovery:
''' bash
while read r; do nc -v -z $r 1-65535; done < $iplist_file
'''