import customtkinter as ctk

def send():
    msg = entry.get().lower()
    entry.delete(0, "end")
    if msg:
        bot.insert("end", f"You: {msg}\n")
        if "hi" in msg or "hello" in msg:
            bot.insert("end", "Bot: Welcome to our restaurant! How can I assist you today?\n")
        elif "what is on the menu" in msg:
            bot.insert("end", "Bot: We serve biryani, pizza, pasta, noodles, and desserts.\n")
        elif "what are your timings" in msg:
            bot.insert("end", "Bot: We're open from 12PM to 11PM, all days of the week.\n")
        elif "do you offer home delivery" in msg:
            bot.insert("end", "Bot: Yes, we deliver through Zomato and Swiggy.\n")
        elif "thankyou" in msg or "thanks" in msg:
            bot.insert("end", "Bot: You're welcome! Let me know if you have any more questions.\n")
        elif "bye" in msg or "exit" in msg:
            bot.insert("end", "Bot: Thank you for visiting! Have a great day!\n")
        else:
            bot.insert("end", "Bot: I'm sorry, I didn't understand that. Can you ask something else?\n")

# Appearance settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("Restaurant Service Chatbot")

bot = ctk.CTkTextbox(master=app, width=380, height=350, wrap="word")
bot.pack(pady=10)
bot.insert("end", "Bot: Hello! How can I help you?\n")

input_frame = ctk.CTkFrame(master=app)
input_frame.pack(pady=10)

entry = ctk.CTkEntry(master=input_frame, width=250, placeholder_text="Type your message...")
entry.pack(side="left", padx=10)

button = ctk.CTkButton(master=input_frame, text="Send", command=send)
button.pack(side="left")

app.mainloop()
