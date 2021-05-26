import os
import time

ask = input("If you want to shutdown your computer, type yes  ").lower()

if ask == "yes":
    os.system("shutdown /s /t 0") # shutdown is the program, /s is the argument for shuting it down,
    # /t is the argument for time, 0 is for time. If you entered 30, it would shutdown the computer in 30 seconds. If
    # you passed /r, it would restart, if you want to log off, that would be /l
else:
    print("program is exiting...")
    time.sleep(3)