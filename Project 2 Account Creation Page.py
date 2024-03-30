import tkinter as tk
from tkinter import messagebox

def create_account():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    country = country_entry.get()
    terms_checked = terms_var.get()

    if not name or not email or not password or not country:
        messagebox.showwarning("Error", "Please fill in all fields.")
    elif not terms_checked:
        messagebox.showwarning("Error", "Please accept the terms and conditions.")
    else:
        # Here, you can add code to process the account creation, such as saving the data to a file or database
        messagebox.showinfo("Success", "Account created successfully! Welcome To Bulls-Eye!")

root = tk.Tk()
root.title("REGISTRATION")  # Set window title to "REGISTRATION"

# Labels
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Label(root, text="Country:").pack()
country_entry = tk.Entry(root)
country_entry.pack()

# Checkbutton for terms and conditions
terms_var = tk.BooleanVar()
terms_checkbox = tk.Checkbutton(root, text="I have read and accept the terms and conditions to using Bulls-Eye.", variable=terms_var)
terms_checkbox.pack()

# Create account button
create_button = tk.Button(root, text="Create Account", command=create_account)
create_button.pack(pady=10)

root.mainloop()
