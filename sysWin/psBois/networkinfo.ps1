"========== NETWORK INFO =========="

$macadress = (Get-WmiObject win32_networkadapterconfiguration | Where-Object { $_.IPEnabled -eq $True} | select macaddress | ft -HideTableHeaders | Out-String).Trim()
Write-Host "Macadress: " -NoNewLine
Write-Host $macadress 

"`n"
$internalIp = (Get-NetIPAddress -InterfaceAlias Ethernet -AddressFamily IPv4 | Select-Object IPAddress | ft -HideTableHeaders | Out-String).Trim()
Write-Host "internal ip: " $internalip

$externalip = (Invoke-WebRequest https://ifconfig.me/ip).Content.Trim()
Write-Host "External ip :" $externalip

"`n"


"========== DONE =========="


