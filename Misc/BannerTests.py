# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:42:17 2017

@author: Tyler

Messing around with animated banner thingies

"""

import os
import time

spaces = 0
spaceLimit = 6

banner = """\
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░          _____   _____          _   _          ░
░    /\   |  __ \ / ____|   /\   | \ | |   /\    ░
░   /  \  | |__) | |       /  \  |  \| |  /  \   ░
░  / /\ \ |  _  /| |      / /\ \ | . ` | / /\ \  ░
░ / ____ \| | \ \| |____ / ____ \| |\  |/ ____ \ ░
░/_/    \_|_|  \_\\\_____/_/    \_|_| \_/_/    \_\░
░            --Tyler Thomas - 2017--             ░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

fuckYou = """\









////////////////////FUCK YOU!/////////////////////

"""



while spaces < spaceLimit:
    
    os.system('cls')
    
    for space in range(spaces):
    
        print()
    
    print(banner)
    
    time.sleep(0.3)
    
    os.system('cls') 
    
    spaces += 1
    
print(fuckYou)
time.sleep(0.2)
os.system('cls')