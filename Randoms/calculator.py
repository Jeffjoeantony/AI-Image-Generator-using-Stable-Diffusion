import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()  #Initialize window
        
        self.title("Calculator")
        self.geometry("300x400")
        self.resizable(False,False)
        
        self.expression = ""

        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Arial",20), justify="right")
        self.entry.place(x=10, y=20)

        buttons = [
            ('AC', 20, 90), ('Del', 85, 90), ('%', 150, 90), ('/', 215, 90),
            ('7', 20, 150), ('8', 85, 150), ('9', 150, 150), ('x', 215, 150),
            ('4', 20, 210), ('5', 85, 210), ('6', 150, 210), ('-', 215, 210),
            ('1', 20, 270), ('2', 85, 270), ('3', 150, 270), ('+', 215, 270),
            ('0', 20, 330), ('.', 85, 330), ('=', 150, 330),
        ]
        
        for(text,x,y) in buttons:
            self.create_button(text,x,y)

    def create_button(self, text, x, y):
        width = 125 if text == '=' else 60

        btn = ctk.CTkButton(self, text=text, width=width, height=50, font=("Arial", 18),
                            fg_color='black',text_color='white',command=lambda: self.on_button_click(text))
        btn.place(x=x, y=y)

    def click_function(self,char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.entry.delete(0,'end')
                self.entry.insert(0,result)
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
        
        
app = Calculator()
app.mainloop()