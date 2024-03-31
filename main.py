import  WelcomePage
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Project 2")
window.geometry("1000x700")
window.resizable(0, 0)

# Create an instance of the WelcomePage class
welcome_page = WelcomePage.WelcomePageClass(window)
welcome_page.drawWidgets()


window.mainloop()