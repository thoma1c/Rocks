# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:16:28 2017

@author: Owner
"""

import winsound
import time
#import math

frequency = 2000
duration = 250

beeps = 5

while beeps > 0:

    winsound.Beep(frequency,duration)
    #time.sleep(0.001)
    
    frequency += 500
    
    beeps -= 1