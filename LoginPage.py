# CCT211: Project 2, Login Page

import tkinter as tk
from tkinter import *
import  WelcomePage
import InvestmentScreen
import acountManagement
import os

class LoginPageClass():

    def __init__(self,window):
        # Get the current working directory
        self.current_directory = os.path.dirname(__file__)
        self.w = window
        # Get the current working directory
        self.current_directory = os.path.dirname(__file__)
        self.window = tk.Frame(self.w)
        self.window.configure(bg="black")
        # Load the logo image
        self.logo_image = tk.PhotoImage(file=os.path.join(self.current_directory, "logo.png"))
        self.logo_image = self.logo_image.subsample(9)

        # Stylize labels and entries
        self.logo_label = tk.Label(self.window, image=self.logo_image, bg="black")
        self.subheading_label = tk.Label(self.window, text="Login to your Account", font=("SF Pro Text", 30), bg="black", fg="white")
        self.username_label = tk.Label(self.window, text="Username:", font=("SF Pro Text", 16), bg="black", fg="white")
        self.username_entry = tk.Entry(self.window, font=("SF Pro Text", 16))
        self.password_label = tk.Label(self.window, text="Password:", font=("SF Pro Text", 16), bg="black", fg="white")
        self.password_entry = tk.Entry(self.window, show="*", font=("SF Pro Text", 16))
        self.buttonframe = tk.Frame(self.window, width=1000, bg="black")
        self.back_home_button = tk.Button(self.buttonframe, text="Back", command=self.back_home, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
        self.login_button = tk.Button(self.buttonframe, text="Login", command=self.login, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
        self.title_label = tk.Label(self.window, text="Welcome Back", bg="black", fg="orange", font=("SF Pro Text", 45))

    # Define back button and login fucntions 
    def back_home(self):
        self.window.pack_forget()  
        WelPage = WelcomePage.WelcomePageClass(self.w)
        WelPage.drawWidgets()
    def login(self):
        
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        if(acountManagement.checkExistinAcount(username)):
            b, acount = acountManagement.login(username, password)
            if b:
                self.window.pack_forget()  
                InvPage = InvestmentScreen.InvestmentScreenClass(self.w, acount)
                InvPage.drawWidgets()
            else:
                #add a login failed message in label
                print("Login failed")
                
    # Placements
    def drawWidgets(self):
        self.window.update()
        self.window.update_idletasks()
        self.window.pack(fill="both", expand=True)

        self.logo_label.place(relx=0.06, rely=0.07)
        self.subheading_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        self.username_label.place(relx=0.3, rely=0.45)
        self.username_entry.place(relx=0.45, rely=0.45)
        self.password_label.place(relx=0.3, rely=0.5)
        self.password_entry.place(relx=0.45, rely=0.5)
        self.buttonframe.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.back_home_button.pack(side=tk.LEFT, padx=(100, 10))
        self.login_button.pack(side=tk.RIGHT, padx=(10,100))
        self.title_label.place(relx=0.23, rely=0.12)

