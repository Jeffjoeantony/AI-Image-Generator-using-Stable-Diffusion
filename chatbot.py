import customtkinter as ctk
import pyttsx3 as pyt
from PIL import Image, ImageTk, ImageDraw

def profile_pic():
    img = Image.open(image_path).resize(size,size), Image.LANCZOS


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("MyBot")
app.configure(bg="white")
top_pad = ctk.CTkFrame(app, fg_color="#007BFF", height=85, corner_radius=0)  # Bootstrap blue
top_pad.pack(fill="x", side="top")

profile = profile_pic("D:/AJCE/1692089610777 (1).jpg",60)


app.mainloop()