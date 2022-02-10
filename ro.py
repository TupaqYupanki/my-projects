
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
<<<<<<< HEAD
    z = pyautogui.locateCenterOnScreen('egggg.png', region=(0,0,1400,800), confidence=0.8)
    s = pyautogui.locateCenterOnScreen('egggg.png', region=(0,0,1400,800), confidence=0.78)
    #a = pyautogui.locateCenterOnScreen('antonio1.png', confidence=0.7)
    # if pyautogui.locateOnScreen('egggg.png', confidence=0.8) != None:
    if z != None and i < 5:
        x,y = z
        pyautogui.moveTo(x,y,0.13)
        pyautogui.click(x,y)
        print('found it')
        i = i+1
        time.sleep(random.uniform(1.6, 1.8))
    elif s != None and i < 5:
        x,y = s
        pyautogui.moveTo(x,y,0.13)
        pyautogui.click(x,y)
        print('found it')
        i = i+1
        time.sleep(random.uniform(1.6, 1.8))
    # elif a != None:
    #     x,y = a
    #     pyautogui.moveTo(x,y,0.13)
    #     pyautogui.click(x,y)
    #     print('found antonio')
    #     time.sleep(random.uniform(11.6, 12.8))
=======
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
>>>>>>> f0622a402433746496e17e3b7b9f2cf1999b33b7
    else:
        i = 0
        print("I am unable to see it")
        pyautogui.press('f1')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(random.uniform(0.4, 0.7))
<<<<<<< HEAD
        if pyautogui.pixel(660, 426)[0] == 66:
            pyautogui.press('insert')
            time.sleep(random.randint(90, 130))
            pyautogui.press('insert')


# while keyboard.is_presse('q') == False:
# pic = pyautogui.screenshot(region=(330, 220, 1250, 650))
# pic.save(r"D:\GIT\my-projects\screeenshot.png")
#pyautogui.displayMousePosition()


    # elif pyautogui.locateOnScreen('egg2.png', confidence=0.8) != None:
    #     pyautogui.click(pyautogui.locateOnScreen('egg2.png', confidence=0.8))
    #     print('found it')
    #     time.sleep(random.uniform(1.3, 1.7))
    # elif pyautogui.locateOnScreen('picky.png', confidence=0.88) != None:
    #     time.sleep(0.02)
    #     pyautogui.click(pyautogui.locateOnScreen('picky.png', confidence=0.88))
    #     print('found it')
    #     time.sleep(random.uniform(0.7, 1))
    # elif pyautogui.locateOnScreen('picky2.png', confidence=0.85) != None:
    #     time.sleep(0.02)
    #     pyautogui.click(pyautogui.locateOnScreen('picky2.png', confidence=0.85))
    #     print('found it')
    #     time.sleep(random.uniform(1, 1.5))
=======
        if pyautogui.pixel(657, 426)[0] == 66:
            pyautogui.press('insert')
            time.sleep(random.randint(90, 130))
            pyautogui.press('insert')
>>>>>>> f0622a402433746496e17e3b7b9f2cf1999b33b7
