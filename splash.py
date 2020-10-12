# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:21:15 2017

@author: Owner
"""

import os
import time
#import winsound



frequency = 2000
duration = 500

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

def printBanner():
    
    print(banner)



os.system('cls')

print(banner)
#winsound.Beep(frequency,duration)

time.sleep(1.5)

os.system('cls')


