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
timer = 0
def feed():
    print("Feeding")
    pyautogui.keyDown('alt')
    time.sleep(0.2)
    pyautogui.press('r')
    time.sleep(0.2)
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
    if feed_timer >= 600:
        feed()
        feed_timer = 0
        timer = time.perf_counter()
    else:
        feed_timer = time.perf_counter() - timer
        print ('feed timer = '+str(feed_timer))
        print("Teleportation")
        pyautogui.click(623,412)
        pyautogui.press('f1')
        time.sleep(0.1)
        pyautogui.press('enter')

        t=0
        z=0
        time.sleep(4)
        if pyautogui.locateCenterOnScreen('teleport.png', region=(116, 744, 55, 20), confidence=0.9) != None:
            print('empty')
        else:
            while ((pyautogui.pixel(716, 419)[1] != 239) and (pyautogui.pixel(716, 423)[1] != 239) and (pyautogui.pixel(716, 422)[1] != 239) and (pyautogui.pixel(716, 413)[1] != 239)) and t<=3 and feed_timer <= 600:
                if z == 2:
                    pyautogui.click(623,427)
                    t=t+1
                # if z == 16:
                #     pyautogui.click(738,413)
                #     t=t+1
                if pyautogui.pixel(95, 83)[0] == 214:
                    print('heal')
                    pyautogui.press('f2')
                    time.sleep(1)
                    for i in range(5):
                        pyautogui.press('f3')
                        pyautogui.click(685,360)
                        time.sleep(0.3)
                else:
                    feed_timer = time.perf_counter() - timer
                    print('feed_timer = '+str(feed_timer))
                    print('t = '+str(t))
                    print('z = '+str(z))
                    time.sleep(2)
                    t=t+1
                    z=z+1


# while keyboard.is_presse('q') == False:
# pic = pyautogui.screenshot(region=(330, 220, 1250, 650))
# pic.save(r"D:\GIT\my-projects\screeenshot.png")
#pyautogui.displayMousePosition()
