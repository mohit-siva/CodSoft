import tkinter as tk
from datetime import datetime

def add_task():
    task = entry.get()
    date_str = date_entry.get()
    time_str = time_entry.get()

    if task and date_str and time_str:
        datetime_str = f"{date_str} {time_str}"
        try:
            task_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            formatted_task = task_datetime.strftime("%Y-%m-%d %H:%M:%S") + f": {task}"
            listbox.insert(tk.END, formatted_task)
            entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            time_entry.delete(0, tk.END)
        except ValueError:
            print("Invalid date or time format. Please use YYYY-MM-DD HH:MM")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create UI elements
entry = tk.Entry(root, width=40)
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_entry = tk.Entry(root, width=20)
time_label = tk.Label(root, text="Time (HH:MM):")
time_entry = tk.Entry(root, width=20)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60)

# Place UI elements in the window
entry.pack(pady=10)
date_label.pack()
date_entry.pack()
time_label.pack()
time_entry.pack()
add_button.pack()
remove_button.pack()
listbox.pack()

# Start the main event loop
root.mainloop()