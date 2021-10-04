#!/usr/bin/env python3

import pyautogui
import sys
import os

try:
    size = pyautogui.size()

    pyautogui.moveTo(size.width/2, size.height/2)

    while True:
        pyautogui.moveRel(0, 200, duration=3)
        pyautogui.moveRel(200, 0, duration=3)
        pyautogui.moveRel(0, -200, duration=3)
        pyautogui.moveRel(-200, 0, duration=3)
except KeyboardInterrupt:
    print('\r  ')
    sys.exit(0)