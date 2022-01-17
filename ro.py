from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

while 1:
    if pyautogui.locateOnScreen('joker1.png', confidence=0.8) != None:
        # print(pyautogui.locateOnScreen('joker1.png', confidence=0.8))
        # x, y = pyautogui.locateCenterOnScreen('joker1.png', confidence=0.8)
        # print(x, y)
        # time.sleep(0.2)
        pyautogui.click(pyautogui.locateCenterOnScreen(
            'joker1.png', confidence=0.8))
        print('found it')
        time.sleep(random.uniform(2.5, 3.5))
        if pyautogui.pixel(938, 596)[0] == 66:
            pyautogui.press('insert')
            time.sleep(random.randint(250, 400))
            pyautogui.press('insert')
    else:
        print("I am unable to see it")
        pyautogui.press("f1")
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(random.uniform(0.6, 1.6))


# 938.596
# 66 66 66
# 24 99 222
# 988 596
# while keyboard.is_presse('q') == False:
# pic = pyautogui.screenshot(region=(330, 220, 1250, 650))
# pic.save(r"D:\GIT\my-projects\screeenshot.png")
#pyautogui.displayMousePosition()
