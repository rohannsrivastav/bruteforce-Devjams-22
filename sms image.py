import subprocess
import threading
from ppadb.client import Client as AdbClient

# def printit():
# threading.Timer(10.0, printit).start()
procId = subprocess.Popen('adb shell', stdin = subprocess.PIPE)

# For Mobile rishab
    # command1="am start -a android.intent.action.SENDTO -d sms:BT-INDBNK" #Rishabh
command="am start -a android.intent.action.SENDTO -d sms:QP-HDFCBK" #Rohan
    # command="screencap /sdcard/screenshot-01.png" #Rohan

command_bytes=str.encode(command)
procId.communicate(command_bytes)

# printit()
import sms_sreen_shot