#press escape to clear the calculator screen
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"])
import tkinter as tk
from math import sin, cos, tan, log, exp, sqrt, pi, e, log2

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg="lightgrey")
        self.attributes("-fullscreen", False)
        self.current_input = ""
        self.create_widgets()
        self.bind_keys()
        
    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=22, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=5)
        self.buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('log', 4, 4),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('sqrt', 5, 3), ('exp', 5, 4),
            ('pi', 6, 0), ('e', 6, 1), ('log2', 6, 2),
            ('EXIT', 6, 3)
        ]
        bold_font = ("Arial", 12, "bold")
        for (text, row, col) in self.buttons:
            if text == "=":
                button = tk.Button(self, text=text, padx=20, pady=20, bg="lightblue", font=bold_font, command=self.calculate_result)
            elif text == "C":
                button = tk.Button(self, text=text, padx=20, pady=20, bg="lightcoral", font=bold_font, command=self.clear_display)
            elif text == "EXIT":
                button = tk.Button(self, text=text, padx=20, pady=20, bg="red", font=bold_font, command=self.quit)
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
                continue
            else:
                button = tk.Button(self, text=text, padx=20, pady=20, bg="lightgrey", font=bold_font, command=lambda txt=text: self.on_button_click(txt))
            button.grid(row=row, column=col, sticky="nsew")
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
    def bind_keys(self):
        self.bind('<Return>', lambda event: self.calculate_result())
        self.bind('<Key>', self.on_key_press)
        self.bind('<Escape>', lambda event: self.clear_display())
    def on_key_press(self, event):
        char = event.char
        if char.isdigit() or char in "+-*/().":
            self.current_input += char
            self.update_display()
        elif char == '\r':
            self.calculate_result()
        elif char == '\x08':
            self.current_input = self.current_input[:-1]
            self.update_display()
    def on_button_click(self, char):
        if char in "0123456789+-*/().":
            self.current_input += char
        elif char == 'pi':
            self.current_input += str(pi)
        elif char == 'e':
            self.current_input += str(e)
        elif char == 'sin':
            self.current_input += 'sin('
        elif char == 'cos':
            self.current_input += 'cos('
        elif char == 'tan':
            self.current_input += 'tan('
        elif char == 'log':
            self.current_input += 'log('
        elif char == 'exp':
            self.current_input += 'exp('
        elif char == 'sqrt':
            self.current_input += 'sqrt('
        elif char == 'log2':
            self.current_input += 'log2('
        self.update_display()
    def calculate_result(self):
        try:
            result = self.evaluate(self.current_input)
            self.current_input = str(result)
        except Exception as e:
            self.current_input = "Error"
            print(f"Error occurred: {e}")
        self.update_display()
    
    def evaluate(self, expression):
        return eval(expression, {'__builtins__': None}, {'sin': sin, 'cos': cos, 'tan': tan, 'log': log, 'exp': exp, 'sqrt': sqrt, 'log2': log2, 'pi': pi, 'e': e})
    
    def clear_display(self):
        self.current_input = ""
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
