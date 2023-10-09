import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Create and configure result label
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.create_result_label()

        # Define buttons and their layout, including the "AC" button
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'AC'
        ]

        # Create buttons grid
        self.create_buttons_grid()

        # Bind keyboard events
        self.root.bind("<Key>", self.on_key_press)

        # Customize button style
        self.customize_button_style()

    def create_result_label(self):
        self.result_label = ttk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 20), anchor="e")
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def create_buttons_grid(self):
        self.row_index = 1
        self.col_index = 0
        for button_text in self.buttons:
            if button_text == 'AC':
                ttk.Button(self.root, text=button_text, command=self.clear_result).grid(row=self.row_index, column=self.col_index, padx=5, pady=5, sticky='nsew', ipadx=10, ipady=10)
            else:
                ttk.Button(self.root, text=button_text, command=lambda text=button_text: self.on_button_click(text)).grid(row=self.row_index, column=self.col_index, padx=5, pady=5, sticky='nsew', ipadx=10, ipady=10)
            self.col_index += 1
            if self.col_index > 3:
                self.col_index = 0
                self.row_index += 1

    def customize_button_style(self):
        style = ttk.Style()
        style.configure('TButton', padding=(0, 10, 0, 10), font=('Helvetica', 16), foreground='blue', background='light yellow')
        style.map('TButton', background=[('active', 'light blue'), ('!disabled', 'light yellow')])

    def on_button_click(self, text):
        if text == '=':
            self.calculate_result()
        else:
            self.update_result_text(text)

    def calculate_result(self):
        try:
            expression = self.result_var.get()
            result = str(eval(expression))
            self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")

    def update_result_text(self, text):
        current_text = self.result_var.get()
        if current_text == '0' and text != '.':
            self.result_var.set(text)
        else:
            self.result_var.set(current_text + text)

    def clear_result(self):
        self.result_var.set("0")

    def on_key_press(self, event):
        key = event.char
        if key in self.buttons:
            self.on_button_click(key)

def main():
    root = tk.Tk()
    app = Calculator(root)
    # Configure row and column weights for button resizing
    for i in range(4):
        root.grid_rowconfigure(i + 1, weight=1)
        root.grid_columnconfigure(i, weight=1)
    root.mainloop()

if __name__ == "__main__":
    main()
