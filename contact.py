import tkinter as tk

# Initialize an empty contact list as a list of dictionaries
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    clear_entries()
    update_contact_listbox()
    status_label.config(text=f"{name} added to contacts.")

# Function to view the contact list
def view_contacts():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

# Function to update the contact listbox
def update_contact_listbox():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

# Function to clear input entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create a Tkinter window
root = tk.Tk()
root.title("Contact Book")

# Labels and Entry Widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack()

# Contact Listbox
contact_listbox = tk.Listbox(root)
contact_listbox.pack()

# Status Label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Start the Tkinter main loop
root.mainloop()
