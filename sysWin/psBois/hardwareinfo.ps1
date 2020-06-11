"========== HARDWARE INFO =========="
Write-Host "COMPUTERS GPU"
$GPU = Get-WmiObject Win32_VideoController | Select Caption, CurrentRefreshRate, DriverVersion | Format-List
$GPU

Write-Host "COMPUTERS CPU"
$CPU = Get-WmiObject Win32_Processor | Select Name, NumberOfCores, CurrentClockSpeed | Format-List
$CPU

Write-Host "ALL NETWORK CARDS"
$allnic = Get-NetAdapter | Select InterfaceDescription, MacAddress, LinkSpeed | Format-List
$allnic

Write-Host "ACTIVE NETWORKCARDS"
$activenic = Get-NetAdapter | Select InterfaceDescription, Status | 
Where-Object {$_.Status -eq "Up"} | Format-List
$activenic

"`n"
Write-Host "FREE/TOTAL MEMORY"
$free =  [math]::Round((Get-CimInstance -Classname Win32_OperatingSystem).FreePhysicalMemory /1GB,3) * 1000
$total = [math]::Round((Get-CimInstance -Classname Win32_OperatingSystem).TotalVisibleMemorySize /1GB,3) * 1000
Write-Host "Free Memory(GB): " $free 
Write-Host "Total Memory(GB): " $total

$ram = Get-Ciminstance Win32_PhysicalMemory 
foreach($i in $ram){
$ramlist = [PsCustomObject]@{
    Type = $i.Description 
    Vendor = $i.Manufacturer
    'Size(GB)' = $i.Capacity /1GB
    }
    $ramlist | Format-List
}
   
Write-Host "HARDDRIVES"
$diskinfo = Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType = 3" 
foreach ($disk in $diskinfo) {

    $part = Get-CimAssociatedInstance -InputObject $disk -ResultClass Win32_DiskPartition
    $drive = Get-CimAssociatedInstance -InputObject $part -ResultClassName Win32_DiskDrive

    [PsCustomObject]@{
        Type = "Hard Drive"
        Model = $drive.Model
        SerialNUmber = $drive.SerialNumber
        'DiskSize(GB)' = [math]::Round(($drive.Size / 1GB ), 2)
        BootPartition = $part.BootPartition
        'PartitionSize(GB)' = [math]::Round(($part.Size / 1GB ), 2)
        DriveLetter = $disk.Caption
        FileSystem = $disk.FileSystem
        Size =  [math]::Round(($disk.Size / 1GB ), 2)
        Free =  [math]::Round(($disk.FreeSpace / 1GB ), 2)
   }
}

"`n"
Write-Host "MOTHERBOARD"
$mb = Get-CimInstance -Class Win32_BaseBoard 
$bios = Get-Ciminstance -Class Win32_Bios
$uuid = (get-wmiobject Win32_ComputerSystemProduct).UUID
$mblist = [PsCustomObject]@{
        Manufacturer = $mb.Manufacturer
        Model = $mb.Product
        Bios = $bios.Version
        UUID = $uuid

        }
    $mblist | Format-List

"`n"
Write-Host "========== DONE =========="


