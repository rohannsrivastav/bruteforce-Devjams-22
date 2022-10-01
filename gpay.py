import subprocess
import threading
from ppadb.client import Client as AdbClient

def printit():
    threading.Timer(5.0, printit).start()
    procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE)

# For Mobile rishab
    command1=" am force-stop com.google.android.apps.nbu.paisa.user" #gpay
    command2=" am force-stop net.one97.paytm"  #paytm

#for Mobile rohan
    command3=" am force-stop com.google.android.apps.nbu.paisa.user" #gpay
    command4=" am force-stop net.one97.paytm" #paytm
    # command_bytes1=str.encode(command1)
    command_bytes2=str.encode(command3)
    procId.communicate(command_bytes2)
    # procId.communicate(command_bytes1)
    
printit()