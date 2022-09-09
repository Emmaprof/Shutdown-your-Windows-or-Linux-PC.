import os
import platform

def shutdown():
    if platform.system() == 'Windows':
        os.system('shutdown -s')
    elif platform.system == "Linux" or platform.system() == "Darwin":
        os.system('shutdown -h now')
    else:
        print("Welcome, os not supported! ")

def restart():
    if platform.system() == 'Windows':
        os.system("shutdown -t O -r -f")
    elif platform.system() == "Linux" or platform.system() == 'Darwin':
        os.system("reboot")
    else:
        print("Emmanuel William, os not supported! ")

command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command =="r":
    restart()
elif command == "s":
    shutdown()
else:
    print(" William, wrong letter! ")

