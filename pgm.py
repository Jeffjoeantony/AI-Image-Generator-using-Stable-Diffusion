import customtkinter as ctk 
import pyautogui 
import time

def send():
    # print("Working....")
    msg = entry.get()
    count = int(entry2.get())
    time.sleep(5)
    for i in range(count):
        pyautogui.typewrite(msg)
        pyautogui.press("Enter")


ctk.set_appearance_mode("System")   #Launch in size of system
ctk.set_default_color_theme("blue")     #Window color

app = ctk.CTk()     #To create a window
app.geometry("900x300")     #Size of window
app.title("MyApp")      #Title of window

label = ctk.CTkLabel(app, text="MyApp", font=("Arial",18))
label.pack(pady=20)     #position

entry = ctk.CTkEntry(app,placeholder_text="Enter Message:",width=250)
entry.pack(pady=20)

entry2 = ctk.CTkEntry(app,placeholder_text="Enter count:",width=250)
entry2.pack(pady=20)

btn = ctk.CTkButton(app,text="SEND",command=send)
btn.pack(pady=20)




app.mainloop()