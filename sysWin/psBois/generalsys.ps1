"========== GENERAL SYSTEM INFO =========="

"`n"

"Current User: "+$env:USERNAME

$getadmin = net localgroup Administrators | 
Where-Object {$_ -and $_ -notmatch "command completed successfully"} | 
ft -HideTableHeaders | select -Skip 5 | Out-String
Write-host "Administators on the computer: "$getadmin

$GeneralOSInfo = Get-CimInstance -Classname Win32_OperatingSystem | 
Select Caption, Version, InstallDate, LocalDateTime, LastBootUpTime, CSName | Format-List
$GeneralOSInfo

"`n"

Write-Host "========== DONE =========="