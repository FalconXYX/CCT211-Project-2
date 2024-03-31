# CCT211: Project 2, Login Page

import tkinter as tk
from tkinter import *

import os


# Get the current working directory
current_directory = os.path.dirname(__file__)

window = tk.Tk()
window.title("Project 2 - Login Page")

window.geometry("1000x700")
window.configure(bg="black")

# Define back button and login fucntions 
def back_home():
    print("Back")
def login():
    print("Login")
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

# Load the logo image
logo_image = tk.PhotoImage(file=os.path.join(current_directory, "logo.png"))
# Resize the image by a factor of 2
logo_image = logo_image.subsample(9)

# Logo label
logo_label = tk.Label(window, image=logo_image, bg="black")
logo_label.place(relx=0.06, rely=0.07)

# Subheading label
subheading_label = tk.Label(window, text="Login to your Account", font=("SF Pro Text", 30), bg="black", fg="white")
subheading_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER) 

# Username label and entry
username_label = tk.Label(window, text="Username:", font=("SF Pro Text", 16), bg="black", fg="white")
username_label.place(relx=0.3, rely=0.45)
username_entry = tk.Entry(window, font=("SF Pro Text", 16))
username_entry.place(relx=0.45, rely=0.45)

# Password label and entry
password_label = tk.Label(window, text="Password:", font=("SF Pro Text", 16), bg="black", fg="white")
password_label.place(relx=0.3, rely=0.5)
password_entry = tk.Entry(window, show="*", font=("SF Pro Text", 16))
password_entry.place(relx=0.45, rely=0.5)


# Frame to hold buttons and title
frame = tk.Frame(window, width=1000, bg="black")
frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


# Create the buttons
back_home_button = tk.Button(frame, text="Back", command=back_home, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
back_home_button.pack(side=tk.LEFT, padx=(100, 10))

login_button = tk.Button(frame, text="Login", command=login, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
login_button.pack(side=tk.RIGHT, padx=(10,100))

# Title label
title_label = tk.Label(window, text="Welcome Back", bg="black", fg="orange", font=("SF Pro Text", 45))
title_label.place(relx=0.23, rely=0.12)

window.mainloop()
