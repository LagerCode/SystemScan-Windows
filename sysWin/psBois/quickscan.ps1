"========== QUICK SCAN =========="

$wdactive = (Get-MpComputerStatus | Select-Object AntivirusEnabled | ft -HideTableHeaders | Out-String).Trim()
Write-Host "Windows Defender Status: " $wdactive
$wdrealtime = (Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled | ft -HideTableHeaders | Out-String).Trim()
Write-Host "Realtime Protection Status: " $wdactive

Update-MpSignature
Write-Host "Updated catalog for virus detection"

$quickscan = Start-MpScan -ScanType QuickScan 

$detected = Get-MpThreatDetection
if ($detected = $null){
    Write-Host "0"
    } else {
    Write-Host "Detected Threats: " $detected
    }

Write-Host "Quickscan Done"