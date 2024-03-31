# CCT211: Project 2, Welcome Page

import tkinter as tk
from tkinter import *

import os


# Get the current working directory
current_directory = os.path.dirname(__file__)

window = tk.Tk()
window.title("Project 2 - Welcome Page")

window.geometry("1000x700")
window.configure(bg="black")

# Define two button functions
def existing_user():
    print("Existing User")
def new_user():
    print("New User")

# Load the logo image
logo_image = tk.PhotoImage(file=os.path.join(current_directory, "logo.png"))
# Resize the image by a factor of 2
logo_image = logo_image.subsample(9)

# Logo label
logo_label = tk.Label(window, image=logo_image, bg="black")
logo_label.place(relx=0.06, rely=0.07)

# Subheading label
subheading_label = tk.Label(window, text="Welcome to Bulls-Eye", font=("SF Pro Text", 35), bg="black", fg="white")
subheading_label.place(relx=0.2, rely=0.1) 

# Caption label
caption_label = tk.Label(window, text="Start managing your investments today", font=("Sans Serif", 17), bg="black", fg="white")
caption_label.place(relx=0.21, rely=0.17) 

# Frame to hold buttons and title
frame = tk.Frame(window, bg="black")
frame.pack(side=tk.BOTTOM, pady=150) 

# Create the buttons
existing_user_button = tk.Button(frame, text="Existing User", command=existing_user, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
existing_user_button.grid(row=0, column=0, padx=(0,100))

new_user_button = tk.Button(frame, text="New User", command=new_user, bg="white", fg="black", font=("SF Pro Text", 18, "bold"))
new_user_button.grid(row=0, column=1, padx=(100,0))

# Title label
title_label = tk.Label(window, text="Get Started Today", bg="black", fg="orange", font=("SF Pro Text", 45))
title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

window.mainloop()
