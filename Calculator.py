import tkinter as tk
import math
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish Calculator")
        
        # Set the window size
        self.root.geometry("400x600")
        self.root.config(bg="#f0f0f0")  # Light grey background

        # Memory for M+ and M- functionality
        self.memory_value = 0

        # Display entry
        self.display = tk.Entry(self.root, font=("Helvetica", 24), bd=10, insertwidth=4, width=14, borderwidth=0, relief="flat", justify="right", bg="#ffffff", fg="#333333")
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

        # History listbox for calculation history
        self.calculation_history = tk.Listbox(self.root, height=5, font=("Helvetica", 12), bg="#f0f0f0", borderwidth=0, relief="flat", fg="#333333")
        self.calculation_history.grid(row=1, column=0, columnspan=4, padx=15, pady=5)

        # Create calculator buttons
        self.create_buttons()

    def create_buttons(self):
        # Button text and layout
        buttons = [
            '7', '8', '9', '/', '√',
            '4', '5', '6', '*', '^',
            '1', '2', '3', '-', '%',
            '0', '.', '=', '+', 'C',
        ]

        # Colors and styles for buttons
        num_color = "#ffffff"  # White button color for numbers
        operator_color = "#FFB6C1"  # Light pink color for operators
        equal_color = "#CBC3E3"  # Light purple color for equals

        # Start creating buttons from row 2
        row, col = 2, 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            
            # Choose color based on type of button
            if button.isdigit() or button == '.':
                btn_color = num_color
            elif button == '=':
                btn_color = equal_color
            else:
                btn_color = operator_color

            # Create the buttons with nice padding and fonts
            tk.Button(self.root, text=button, padx=20, pady=20, font=("Helvetica", 18), bg=btn_color, fg="black", 
                      relief="flat", activebackground="#333333", activeforeground="black", 
                      command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            col += 1
            if col > 4:
                col = 0
                row += 1

        # Clear, backspace, memory buttons
        tk.Button(self.root, text='←', padx=20, pady=20, font=("Helvetica", 18), bg="#FF6961", fg="black", 
                  relief="flat", command=self.backspace).grid(row=row, column=0, padx=5, pady=5, sticky="nsew")

        tk.Button(self.root, text='M+', padx=20, pady=20, font=("Helvetica", 18), bg="#DAB1DA", fg="black", 
                  relief="flat", command=lambda: self.memory_function('M+')).grid(row=row, column=1, padx=5, pady=5, sticky="nsew")

        tk.Button(self.root, text='M-', padx=20, pady=20, font=("Helvetica", 18), bg="#DAB1DA", fg="black", 
                  relief="flat", command=lambda: self.memory_function('M-')).grid(row=row, column=2, padx=5, pady=5, sticky="nsew")

        tk.Button(self.root, text='MR', padx=20, pady=20, font=("Helvetica", 18), bg="#DAB1DA", fg="black", 
                  relief="flat", command=lambda: self.memory_function('MR')).grid(row=row, column=3, padx=5, pady=5, sticky="nsew")

        # Make buttons expand to fit window size
        for i in range(5):
            self.root.grid_rowconfigure(i+2, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        current = self.display.get()

        if char == "=":
            try:
                result = eval(current.replace('√', 'math.sqrt').replace('^', '**'))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.calculation_history.insert(tk.END, f"{current} = {result}")
                self.calculation_history.yview(tk.END)  # Auto-scroll to latest calculation
            except:
                messagebox.showerror("Error", "Invalid input")
                self.clear()
        elif char == '√':
            try:
                number = float(current)  # Convert the current display value to a number
                result = math.sqrt(number)  # Calculate the square root
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                messagebox.showerror("Error", "Invalid input for square root")
                self.clear()
        elif char == 'C':
            self.clear()
        else:
            self.display.insert(tk.END, char)

    def clear(self):
        self.display.delete(0, tk.END)

    def backspace(self):
        current = self.display.get()
        if len(current) > 0:
            self.display.delete(len(current) - 1, tk.END)

    def memory_function(self, func):
        current = self.display.get()

        if func == 'M+':
            self.memory_value += float(current)
        elif func == 'M-':
            self.memory_value -= float(current)
        elif func == 'MR':
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.memory_value))

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
