import tkinter as tk
from tkinter import messagebox

# In-memory storage for contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and phone number are required!")
        return

    contacts[name] = {"phone": phone, "email": email, "address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_entries()
    view_contacts()

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Function to search for a contact
def search_contact():
    search_term = entry_search.get().strip().lower()
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details["phone"]:
            contact_list.insert(tk.END, f"{name} - {details['phone']}")
    if not contact_list.size():
        messagebox.showinfo("Search Result", "No contact found!")

# Function to load selected contact into the fields for update
def load_contact(event):
    selected = contact_list.curselection()
    if selected:
        name = contact_list.get(selected).split(" - ")[0]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, name)
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contacts[name]["phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contacts[name]["email"])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contacts[name]["address"])

# Function to update a contact
def update_contact():
    name = entry_name.get().strip()
    if name in contacts:
        contacts[name]["phone"] = entry_phone.get().strip()
        contacts[name]["email"] = entry_email.get().strip()
        contacts[name]["address"] = entry_address.get().strip()
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Function to delete a contact
def delete_contact():
    name = entry_name.get().strip()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.configure(bg="black")

# Style configurations
label_font = ("Arial", 12, "bold")
entry_bg = "#333333"
entry_fg = "white"
button_bg = "#555555"
button_fg = "white"

# Entry fields and labels
tk.Label(root, text="Name:", bg="black", fg="white", font=label_font).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:", bg="black", fg="white", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_phone = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:", bg="black", fg="white", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:", bg="black", fg="white", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_address = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, width=30)
entry_address.grid(row=3, column=1, padx=10, pady=5)

# Buttons for Add, Update, and Delete
add_button = tk.Button(root, text="Add Contact", command=add_contact, bg=button_bg, fg=button_fg, font=label_font, width=15)
add_button.grid(row=4, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact, bg=button_bg, fg=button_fg, font=label_font, width=15)
update_button.grid(row=4, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, bg=button_bg, fg=button_fg, font=label_font, width=15)
delete_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Contact listbox and scrollbar
contact_list = tk.Listbox(root, bg=entry_bg, fg=entry_fg, font=label_font, width=50, height=10)
contact_list.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
contact_list.bind('<<ListboxSelect>>', load_contact)

# Search field and button
tk.Label(root, text="Search:", bg="black", fg="white", font=label_font).grid(row=7, column=0, padx=10, pady=5, sticky="e")
entry_search = tk.Entry(root, bg=entry_bg, fg=entry_fg, font=label_font, width=30)
entry_search.grid(row=7, column=1, padx=10, pady=5)

search_button = tk.Button(root, text="Search", command=search_contact, bg=button_bg, fg=button_fg, font=label_font, width=15)
search_button.grid(row=8, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
