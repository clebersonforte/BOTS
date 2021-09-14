from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#linha 1 = (302,610)
#linha 2 = (388,610)
#linha 3 = (457,610)
#linha 4 = (537,610)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(302,457)[0]==0:
        click(302,457)
    if pyautogui.pixel(388,457)[0]==0:
        click(388,457)
    if pyautogui.pixel(457,457)[0]==0:
        click(457,457)
    if pyautogui.pixel(537,457)[0]==0:
        click(537,457)
    
