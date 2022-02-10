from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
#1360 768
while keyboard.is_pressed('q') == False:
    z = pyautogui.locateCenterOnScreen('porc1.png', region = (0,0,1400,800), confidence=0.65)
    a = pyautogui.locateCenterOnScreen('porc2.png', region = (0,0,1400,800), confidence=0.65)
    b = pyautogui.locateCenterOnScreen('porc3.png', region = (0,0,1400,800), confidence=0.65)
    c = pyautogui.locateCenterOnScreen('porc4.png', region = (0,0,1400,800), confidence=0.65)
    # if pyautogui.locateOnScreen('egggg.png', confidence=0.8) != None:
    if keyboard.is_pressed('w'):
        time.sleep(5)
    elif z != None:
        x, y = z
        # pyautogui.press('f2')
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found z')
        time.sleep(2.3)
    elif a != None:
        x, y = a
        # pyautogui.press('f2')
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found a')
        time.sleep(2.3)
    elif b != None:
        x, y = b
        # pyautogui.press('f2')
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found b')
        time.sleep(2.3)
    elif c != None:
        x, y = c
        # pyautogui.press('f2')
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found b')
        time.sleep(2.3)
    else:
        print("I am unable to see it")
        pyautogui.press('f1')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(random.uniform(0.4, 0.7))
        if pyautogui.pixel(657, 426)[0] == 66:
            pyautogui.press('insert')
            time.sleep(random.randint(90, 130))
            pyautogui.press('insert')
