from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
#1360 768
i = 0
# while keyboard.is_pressed('q') == False:
pic = pyautogui.screenshot(region=(300,100,800,600))
pic.save(r'screensaver.png')

while keyboard.is_pressed('q') == False:
    # pyautogui.click(712, 412)
    # # pyautogui.moveTo(812,410)
    # # time.sleep(0.3)
    a = pyautogui.locateCenterOnScreen('bat1.png', region = (300,100,800,600), confidence=0.8)
    b = pyautogui.locateCenterOnScreen('bat2.png', region = (300,100,800,600), confidence=0.8)
    c = pyautogui.locateCenterOnScreen('bat3.png', region = (300,100,800,600), confidence=0.8)
    d = pyautogui.locateCenterOnScreen('bat4.png', region = (300,100,800,600), confidence=0.8)
    hp = pyautogui.locateCenterOnScreen('hp.png', region = (400,200,600,400), confidence=0.8)
    # if pyautogui.locateOnScreen('egggg.png', confidence=0.8) != None:
    if keyboard.is_pressed('w'):
        time.sleep(5)
    elif hp != None:
        x, y = hp
        pyautogui.click(x, (y-30))
        pyautogui.moveTo(812,410)
        print('found hp')
        time.sleep(6)
    elif a != None:
        x, y = a
        pyautogui.click(x, y)
        pyautogui.moveTo(812,410)
        print('found a')
        time.sleep(6)
    elif b != None:
        x, y = b
        pyautogui.click(x, y)
        pyautogui.moveTo(812,410)
        print('found b')
        time.sleep(6)
    elif c != None:
        x, y = c
        pyautogui.click(x, y)
        pyautogui.moveTo(812,410)
        print('found c')
        time.sleep(6)
    elif d != None:
        x, y = d
        pyautogui.click(x, y)
        pyautogui.moveTo(812,410)
        print('found d')
        time.sleep(6)
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
