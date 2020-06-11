import subprocess, datetime, os, threading
from tkinter import *


#TODO: Add progressbar
#TODO: disable app in order for no crashes with longer operations
'''if os.getuid() == 0:
    True
else:

    sys.exit("u need to run this as root\n"
             "type sudo before running this script")'''

root = Tk()
root.title("SystemHealth")
root.geometry('1200x700')
root.configure(background="#17202A")
getdir = os.getcwd()

def General_SysInfo():
    # Shows users logged in, running distro and how long the system have been up
    try:

        General_Sys = subprocess.Popen(['powershell.exe',
            getdir+ '\\psBois\\generalsys.ps1'],
            stdout=subprocess.PIPE)
        General_SysOutput = General_Sys.communicate()



        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, General_SysOutput)
        display.config(state=DISABLED)

        print("Current Time: " + datetime.now())

    except:

        print("Something went wrong")


def Hw_Info():
    # Shows info about the Motherboard, Gpu,Cpu and Ram
    try:
        Hw = subprocess.Popen(['powershell.exe',
            getdir+ '\\psBois\\hardwareinfo.ps1'],
            shell=False,
            stdout=subprocess.PIPE)
        HwOutput = Hw.communicate()

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, HwOutput)
        display.config(state=DISABLED)

    except:

        print("Something went wrong")


def Net_Info():
    # Shows internal Ip and Mac adress
    try:
        Net = subprocess.Popen(['powershell.exe',
            getdir+ '\\psBois\\networkinfo.ps1'],
            shell=False,
            stdout=subprocess.PIPE)
        NetOutput = Net.communicate()

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, NetOutput)
        display.config(state=DISABLED)

    except:
        print("Something went wrong")


def Check_conn():
    try:
        Connection = subprocess.Popen('speedtest.exe',
                               shell=False,
                               stdout=subprocess.PIPE)
        ConnectionOutput = Connection.communicate()

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, ConnectionOutput)
        display.config(state=DISABLED)
    except:
        print('Something went wrong\n',
              '\n Check if speedtest-cli is installed\n',
              '\n If not, run command "sudo apt install speedtest-cli')


#TODO: se resultat utav scan
def quickScan():
    # Stoppar daemon, uppdaterar databasen i clam, kör heuristic scan
    try:

        FastScan = subprocess.Popen(['powershell.exe',
                          getdir + '\\psBois\\quickscan.ps1'],
                         shell=False,
                         stdout=subprocess.PIPE)
        root.update_idletasks()
        FastScanOutput = FastScan.communicate()

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, FastScanOutput)
        display.config(state=DISABLED)

    except:

        sys.exit('Something went wrong\n')

def fullScan():
    try:
        AllScan = subprocess.Popen(['powershell.exe',
                          getdir + '\\psBois\\fullscan.ps1'],
                         shell=False,
                         stdout=subprocess.PIPE)
        AllscanOutput = AllScan.communicate()

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, AllscanOutput)
        display.config(state=DISABLED)

    except:

        sys.exit('Something went wrong\n')

def repair():
    try:
        WinRepair = subprocess.Popen(['powershell.exe',
                          getdir + '\\psBois\\repair.ps1'],
                         shell=False,
                         stdout=subprocess.PIPE)
        WinREpairOutput = WinRepair.communicate()

        display.config(state=NORMAL)
        display.delete(1.0, END)
        display.insert(INSERT, WinREpairOutput)
        display.config(state=DISABLED)

    except:
        print("something went wrong!")



def scan():
    controlWin = Tk()
    controlWin.geometry('300x200')
    controlWin.configure(background="#17202A")


    quickscanLabel = Label(controlWin,
                           text="Quickscan\n"
                           "time: 2 - 5 min",
                           bg="#17202A",
                           fg="white")
    quickscanLabel.place(x=10, y=30)

    fullscanLabel = Label(controlWin,
                          text="Fullscan\n"
                               "time: 15 - 20 min\n",
                          bg="#17202A",
                          fg="white")
    fullscanLabel.place(x=190, y=30)

    quickscanButton = Button(controlWin,
                             text="Quickscan",
                             command=threading.Thread(target=quickScan).start,
                             bg="#283747",
                             fg="white",
                             relief="flat"
                             )
    quickscanButton.place(x=20, y=80)

    fullscanButton = Button(controlWin,
                             text="Fullscan",
                             command=threading.Thread(target=fullScan).start,
                             bg="#283747",
                             fg="white",
                             relief="flat")
    fullscanButton.place(x=210, y=80)


########################################################################################################################
'''GUI'''
########################################################################################################################

display = Text(root,
                   height=40,
                   width=80,
                   state=DISABLED,
                   bg="#5d6d7e")

MenuLabel = Label(root, text="MENU",
                  fg="white",
                  bg="#17202A")
SystemHealthLabel = Label(root, text="This is a software that let's you see information about your computer",
                          fg="white",
                          bg="#17202A")

General_SysInfoLabel = Label(root,
                                 text="Information about the system")
General_SysInfoButton = Button(root,
                                   text="System Info",
                                   pady=5,
                                   command=threading.Thread(target=General_SysInfo).start,
                                   bg="#283747",
                                   fg="white",
                                   relief="flat")

Hw_InfoLabel = Label(root,
                         text="Information about the hardware in the machine")
Hw_InfoLabelButton = Button(root,
                                text="Hardware Info",
                                pady=5,
                                command=threading.Thread(target=Hw_Info).start,
                                bg="#283747",
                                fg="white",
                                relief="flat")

Net_infoLabel = Label(root, text="See your ip and mac adress")
Net_infoButton = Button(root,
                            text="Network Info",
                            pady=5,
                            command=threading.Thread(target=Net_Info).start,
                            bg="#283747",
                            fg="white",
                            relief="flat")
RepairWinButton = Button(root,
                         text="Repair Windows",
                         pady=5,
                         command=threading.Thread(target=repair).start,
                         bg="#283747",
                         fg="white",
                         relief="flat")

CheckConnection = Label(root, text="Check your connection")
CheckConnectionButton = Button(root,
                            text="Connection Check",
                            pady=5,
                            command=threading.Thread(target=Check_conn).start,
                            bg="#283747",
                            fg="white",
                            relief="flat"
)

Check_For_MalwareLabel = Label(root,
                                   text="Run a scan for malware in your machine",
                                   )
Check_For_MalwareButton = Button(root,
                                     text="Scan",
                                     pady=5,
                                     command=scan,
                                     bg="#283747",
                                     fg="white",
                                     relief="flat")

display.place(x=500, y=40)

MenuLabel.place(x=200, y=20)
SystemHealthLabel.place(x=50, y=60)

#General_SysInfoLabel.grid(row=1, column=1, pady=10)
General_SysInfoButton.place(x=180, y=130)

#Hw_InfoLabel.grid(row=2, column=1, pady=10)
Hw_InfoLabelButton.place(x=180, y=180)

#Net_infoLabel.grid(row=3, column=1, pady=10)
Net_infoButton.place(x=180, y=230)

#CheckConnection.grid(row=4, column=1, pady=10)
CheckConnectionButton.place(x=180, y=280)

RepairWinButton.place(x=180, y=330)

#Check_For_MalwareLabel.grid(row=6, column=1, pady=10)
Check_For_MalwareButton.place(x=180, y=380)


root.mainloop()