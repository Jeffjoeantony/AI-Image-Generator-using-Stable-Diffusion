import pyautogui
import time

while True:
    # x,y = pyautogui.position()
    # print(x,y)
    # time.sleep(1)
    
    pyautogui.moveTo(1186,1049,duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(170,146,duration=1.2)
    pyautogui.click()
    pyautogui.typewrite("NOBODY")
    
    pyautogui.moveTo(239,229,duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(682,986,duration=0.5)
    pyautogui.click()
    for i in range(5):
        pyautogui.typewrite("Podi")
        time.sleep(1)
        pyautogui.press("Enter")
    exit()

    