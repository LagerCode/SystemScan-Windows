"========== FULL SCAN =========="

$wdactive = (Get-MpComputerStatus | Select-Object AntivirusEnabled | ft -HideTableHeaders | Out-String).Trim()
Write-Host "Windows Defender Status: " $wdactive
$wdrealtime = (Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled | ft -HideTableHeaders | Out-String).Trim()
Write-Host "Realtime Protection Status: " $wdactive

Update-MpSignature
Write-Host "Updated catalog for virus detection"

Write-Host "Starting fullscan..."
$fullscan = Start-MpScan -ScanType FullScan
Write-Host "Done"