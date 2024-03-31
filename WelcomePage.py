# CCT211: Project 2, Welcome Page

import tkinter as tk
from tkinter import *

import os
import LoginPage
import AccountCreationPage

# Get the current working directory
class WelcomePageClass():

    def __init__(self,window):
        self.w = window
        # Get the current working directory
        self.current_directory = os.path.dirname(__file__)
        self.window = tk.Frame(self.w)
        self.window.configure(bg="black")
        # Load the logo image
        self.logo_image = tk.PhotoImage(file=os.path.join(self.current_directory, "logo.png"))
        # Resize the image by a factor of 2
        self.logo_image = self.logo_image.subsample(9)
        # Logo label
        self.logo_label = tk.Label(self.window, image=self.logo_image, bg="black")
        # Define two button functions
        self.subheading_label = tk.Label(self.window, text="Welcome to Bulls-Eye", font=("SF Pro Text", 35), bg="black", fg="white")
        self.caption_label = tk.Label(window, text="Start managing your investments today", font=("Sans Serif", 17), bg="black", fg="white")
        self.frame = tk.Frame(self.window, bg="black")
        self.existing_user_button = tk.Button(self.frame, text="Existing User", command=self.existing_user, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
        self.new_user_button = tk.Button(self.frame, text="New User", command=self.new_user, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
        self.title_label = tk.Label(window, text="Get Started Today", bg="black", fg="orange", font=("SF Pro Text", 45))


    def existing_user(self):
        self.window.pack_forget()  
        LogPage = LoginPage.LoginPageClass(self.w)
        LogPage.drawWidgets()
    def new_user(self):
        self.window.pack_forget()  
        AccPage = AccountCreationPage.AccountCreationPageClass(self.w)
        AccPage.drawWidgets()
    def drawWidgets(self):
        self.window.pack(fill="both", expand=True)
        self.logo_label.place(relx=0.06, rely=0.07)

        # Subheading label
        self.subheading_label.place(relx=0.2, rely=0.1) 

        # Caption label
        self.caption_label.place(relx=0.21, rely=0.17) 

        # Frame to hold buttons and title
        self.frame.pack(side=tk.BOTTOM, pady=150) 

        # Create the buttons
        self.existing_user_button.grid(row=0, column=0, padx=(0,100))

        self.new_user_button.grid(row=0, column=1, padx=(100,0))

        # Title label
        self.title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

