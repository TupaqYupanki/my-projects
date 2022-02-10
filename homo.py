from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
#1360 768
time.sleep(2)
feed_timer = 0
def feed():
    print("Feeding")
    pyautogui.keyDown('alt')
    pyautogui.press('r')
    pyautogui.keyUp('alt')
    time.sleep(0.2)
    pyautogui.moveTo(388, 290 ,0.13)
    pyautogui.click(388, 290)
    time.sleep(0.2)
    pyautogui.moveTo(754, 452 ,0.13)
    pyautogui.click(754, 452)
    time.sleep(0.2)
feed()
while keyboard.is_pressed('q') == False:
    if feed_timer == 10:
        feed()
        feed_timer = 0
    else:
        print('feed_timer = '+str(feed_timer))
        pyautogui.click((random.uniform(615, 810)), (random.uniform(350, 455)))
        time.sleep(27.3)
        pyautogui.click((random.uniform(600, 753)), (random.uniform(340, 460)))
        time.sleep(20)
        # pyautogui.click(685, 374)
        # time.sleep(15)
        print("Teleportation")
        feed_timer = feed_timer+1
        pyautogui.press('f1')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(12)





# while keyboard.is_presse('q') == False:
# pic = pyautogui.screenshot(region=(330, 220, 1250, 650))
# pic.save(r"D:\GIT\my-projects\screeenshot.png")
#pyautogui.displayMousePosition()
