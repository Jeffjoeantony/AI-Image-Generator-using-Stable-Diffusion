# RULE BASED CHATBOT

import customtkinter as ctk
import pyttsx3 as pyt
import webbrowser
import time

sp = pyt.init()

def bot():
    msg = entry.get()
    if "Hi" in msg:
        otpt.configure(text="hello")
        sp.say("Hello")
        sp.runAndWait()
    elif("name" in msg):
        sp.say("My name is MyBot")
        otpt.configure(text="My name is MyBot")
        sp.runAndWait()
    elif("What is python" in msg):
        sp.say("Python is a programming language")
        otpt.configure(text="Python is a programming language")
        sp.runAndWait()
    elif("Open my browser" in msg or "Open browser" in msg  or "Open google" in msg or "Search for me" in msg):
        sp.say("Opening")
        otpt.configure(text="Browser starting....")
        webbrowser.open("www.google.com")
        sp.runAndWait()
    else:
        sp.say("I don't know")  
        otpt.configure(text="I don't know")
        sp.runAndWait()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("MyBot")

label = ctk.CTkLabel(app,text="Welcome to MyBot", font=("Arial",18))
label.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="Enter message",width=300)
entry.pack(pady=10)

btn = ctk.CTkButton(app,text="SEND",command=bot)
btn.pack(pady=20)

otpt = ctk.CTkLabel(app,text="", font=("Arial",18),text_color="green")
otpt.pack(pady=20)

app.mainloop()