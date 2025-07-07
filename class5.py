# import pyautogui
# import time

# time.sleep(3)

# # pyautogui.moveTo(200,300)
# pyautogui.moveTo(400,500,duration=1)

# TO OPEN AN APP / TO CLICK AN ITEM

# Finding position
import pyautogui
import time

while True:
    x,y = pyautogui.position()
    print(x,y)
    time.sleep(1)


# import pyautogui
# import time

# msg = ("Hi","How","are","you")

# time.sleep(3)
# pyautogui.moveTo(1182,1049,duration=0.5)
# pyautogui.click()
# for i in msg:
#     pyautogui.typewrite(i)
#     pyautogui.press("Enter")

# import pyttsx3

# sp = pyttsx3.init()

# sp.setProperty("rate",500)
# sp.say("Hi")

# sp.runAndWait()

import webbrowser

webbrowser.open()