import string
import random
import tkinter as tk
from tkinter import ttk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = ttk.Entry(root)
        self.length_entry.pack()

        self.complexity_label = ttk.Label(root, text="Complexity:")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_combo = ttk.Combobox(root, textvariable=self.complexity_var, values=["Easy", "Medium", "Strong"])
        self.complexity_combo.pack()

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.generated_password_label = ttk.Label(root, text="")
        self.generated_password_label.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        if complexity == "Easy":
            characters = string.ascii_letters
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        elif complexity == "Strong":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.generated_password_label.config(text="Generated Password: " + password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
