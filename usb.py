import subprocess, os

def detect_usb():
    while True:
        output = subprocess.check_output("wmic logicaldisk get caption, drivetype", shell=True)
        data = str(output)
        x = data.find("2")
        if not x == -1:
            get = data.find("2")
            cvt = int(get)
            divise = cvt - 9
            getD = data[divise:cvt]
            global lecteur
            lecteur = getD[0:2]
            
            print("Your USB label : ", lecteur, "is connected")
detect_usb()