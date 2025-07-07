import customtkinter as ctk

# Initialize appearance and theme
ctk.set_appearance_mode("light")  # options: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("blue")  # other options: "green", "dark-blue"

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""

        # Entry box
        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Arial", 20), justify="right")
        self.entry.place(x=10, y=20)

        # Buttons layout
        buttons = [
            ('7', 10, 90), ('8', 80, 90), ('9', 150, 90), ('/', 220, 90),
            ('4', 10, 150), ('5', 80, 150), ('6', 150, 150), ('*', 220, 150),
            ('1', 10, 210), ('2', 80, 210), ('3', 150, 210), ('-', 220, 210),
            ('0', 10, 270), ('.', 80, 270), ('=', 150, 270), ('+', 220, 270),
            ('C', 10, 330), 
        ]

        for (text, x, y) in buttons:
            self.create_button(text, x, y)

    def create_button(self, text, x, y):
        btn = ctk.CTkButton(self, text=text, width=60, height=50, font=("Arial", 18), command=lambda: self.on_button_click(text))
        btn.place(x=x, y=y)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, 'end')
                self.entry.insert(0, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, 'end')
                self.entry.insert(0, "Error")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.entry.delete(0, 'end')
        else:
            self.expression += str(char)
            self.entry.delete(0, 'end')
            self.entry.insert(0, self.expression)

# Run the app
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
