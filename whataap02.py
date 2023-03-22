import pyautogui
import time
time.sleep(10)
count =0
while count<=100:
    pyautogui.typewrite("happy holi")
    pyautogui.press("enter")
    count=count+1