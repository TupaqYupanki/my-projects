from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
#1360 768
i = 0
while keyboard.is_pressed('q') == False:
    z = pyautogui.locateCenterOnScreen('egg3.png', region = (0,0,1400,800), confidence=0.8)
    time.sleep(0.03)
    a = pyautogui.locateCenterOnScreen('egg4.png', region = (0,0,1400,800), confidence=0.8)
    time.sleep(0.03)
    b = pyautogui.locateCenterOnScreen('egg5.png', region = (0,0,1400,800), confidence=0.8)
    # if pyautogui.locateOnScreen('egggg.png', confidence=0.8) != None:
    if keyboard.is_pressed('w'):
        time.sleep(5)
    elif z != None and i < 5:
        x, y = z
        pyautogui.moveTo(x, y, 0.13)
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found z')
        i = i+1
        time.sleep(random.uniform(1.8, 2.0))
    elif a != None and i < 5:
        x, y = a
        pyautogui.moveTo(x, y, 0.13)
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found a')
        i = i+1
        time.sleep(random.uniform(1.8, 2.0))
    elif b != None and i < 5:
        x, y = b
        pyautogui.moveTo(x, y, 0.13)
        pyautogui.click(x, y)
        pyautogui.moveTo((x+(random.uniform(0, 30))), (y+(random.uniform(0, 30))), 0.13)
        print('found b')
        i = i+1
        time.sleep(random.uniform(1.8, 2.0))
    else:
        i = 0
        print("I am unable to see it")
        pyautogui.press('f1')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(random.uniform(0.4, 0.7))
        if pyautogui.pixel(657, 426)[0] == 66:
            pyautogui.press('insert')
            time.sleep(random.randint(90, 130))
            pyautogui.press('insert')
