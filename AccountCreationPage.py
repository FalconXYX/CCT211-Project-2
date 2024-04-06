import tkinter as tk
from tkinter import messagebox
import acountManagement
import InvestmentScreen
import os

class AccountCreationPageClass():
    def __init__(self, window):
        self.w = window
        self.current_directory = os.path.dirname(__file__)
        self.window = tk.Frame(self.w)
        self.window.configure(bg="black")
        self.name_entry = tk.Entry(self.window)
        self.email_entry = tk.Entry(self.window)
        self.password_entry = tk.Entry(self.window, show="*")
        self.terms_var = tk.BooleanVar()
        self. nameLabel = tk.Label(self.window, text="Name:", bg="black", fg="white")
        self.terms_checkbox = tk.Checkbutton(self.window, text="I have read and accept the terms and conditions to using Bulls-Eye.", variable=self.terms_var, bg="black", fg="white")
        self.create_button = tk.Button(self.window, text="Create Account", command=self.create_account)
        self.emailLabel = tk.Label(self.window, text="Username:", bg="black", fg="white")
        self.passwordLabel = tk.Label(self.window, text="Password:", bg="black", fg="white")
        self.logo_image = tk.PhotoImage(file=os.path.join(self.current_directory, "logo.png"))
        self.logo_image = self.logo_image.subsample(9)
        self.window.configure(bg="black")
        self.logo_label = tk.Label(self.window, image=self.logo_image, bg="black")


    def create_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        terms_checked = self.terms_var.get()

        if not name or not email or not password:
            messagebox.showwarning("Error", "Please fill in all fields.")
        elif not terms_checked:
            messagebox.showwarning("Error", "Please accept the terms and conditions.")
        else:
            if(acountManagement.checkExistinAcount(email)== False):
                UserAcount = acountManagement.createAcount(email, password, name)
                messagebox.showinfo("Success", "Account created successfully! Welcome To Bulls-Eye!")
                self.window.pack_forget()
                InvPage = InvestmentScreen.InvestmentScreenClass(self.w, UserAcount)
                InvPage.drawWidgets()



            else:
                messagebox.showwarning("Error", "Account already exists!")

    def drawWidgets(self):
        self.window.pack(fill="both", expand=True)
        self.nameLabel.pack()
        self.name_entry.pack()

        self.emailLabel.pack()
        self.email_entry.pack()

        self.passwordLabel.pack()
        self.password_entry.pack()

      
        self.terms_checkbox.pack()

        self.create_button.pack(pady=10)
        self.logo_label.place(relx=0.06, rely=0.07)

