"========== REPAIR =========="
Write-Host "Scanning for system file errors"
sfc /scannow
    

"`n"
clear
Write-Host "Preparing for WIndows Image Repair"

Repair-WindowsImage -Online -ScanHealth

"`n"
clear
Write-Host "Repaing Windows Image"
Repair-WindowsImage -Online -RestoreHealth


"========== DONE =========="