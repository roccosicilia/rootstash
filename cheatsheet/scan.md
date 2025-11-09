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

PowerShell discovery:
''' powershell
param (
    [Parameter(Mandatory = $true)]
    [string]$IPAddress
)

Write-Host "Verifica connettività verso $IPAddress`n" -ForegroundColor Cyan

Write-Host "1. Test ping..." -ForegroundColor Yellow
$pingResult = Test-Connection -ComputerName $IPAddress -Count 2 -Quiet

if ($pingResult) {
    Write-Host "L'indirizzo $IPAddress risponde al ping" -ForegroundColor Green
} else {
    Write-Host "L'indirizzo $IPAddress NON risponde al ping" -ForegroundColor Red
}

function Test-TCPPort {
    param(
        [string]$Target,
        [int]$Port
    )

    try {
        $tcp = New-Object System.Net.Sockets.TcpClient
        $tcp.Connect($Target, $Port)
        $tcp.Close()
        return $true
    } catch {
        return $false
    }
}

$ports = @(80, 443, 8888)

foreach ($port in $ports) {
    Write-Host "`n2. Test porta TCP $port..."
    if (Test-TCPPort -Target $IPAddress -Port $port) {
        Write-Host "Porta $port aperta su $IPAddress" -ForegroundColor Green
    } else {
        Write-Host "Porta $port chiusa o non raggiungibile su $IPAddress" -ForegroundColor Red
    }
}

Write-Host "`nVerifica completata." -ForegroundColor Cyan

'''


