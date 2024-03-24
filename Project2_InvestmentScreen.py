"""
CCT211 Project 2: Investment Screen
"""

# Import tkinter and its functions
import tkinter
from tkinter import *

# --- Set Up

# Setting up the window and its title
window = tkinter.Tk()
window.title("Project 2 - Investment Screen")

# Defining the size of the window using the "geometry" function
window.geometry("1000x700")

# --- Classes Within The Program

# Class for all buttons within the program
class UniversalButton(Button):
    
    def __init__(self, master, text, command, fg, **kwargs):
        super().__init__(master, text=text, command=command, fg=fg)
        
        self['text'] = text
        self['command'] = command
        self['fg'] = fg
        
        self.config(**kwargs)

# Class for all labels within the program
class UniversalLabel(Label):
    
    def __init__(self, master, text, fg, **kwargs):
        super().__init__(master, text=text, fg=fg)
        
        self['text'] = text
        self['fg'] = fg
        
        self.config(**kwargs)

# --- Program Functions

# Testing function
# Replaced later for actual functions
def tester():
    print("This is a test, and it has worked")

# Input vaildation function for letters only
def input_val_text(inp):
    if inp.isalpha():
        return True
    
    elif inp == "":
        return True
    
    else:
        return False

# Input vaildation function for number only
def input_val_num(inp):
    if inp.isnumeric():
        return True
    
    elif inp == "":
        return True
    
    else:
        return False

''' --- The Program Itself --- '''

# --- Title + Search Bar

# Setting up where these two assets will go
title_and_search = Frame(window, width = 900, height = 100)

# Setting up the text that displays the name of the screen
title = UniversalLabel(title_and_search, "Investment Tracker", "black")

# Setting up the search bar via an entry field
searchbar = Entry(title_and_search, width = 10)

'''
# Putting the input vaildation function for this search bar
searchbar_reg = window.register(input_val_text)
searchbar.configure(validate = "key",vcmd = (reg,"%P"))
'''

# The view button for when the user types into the entry field
view_button = UniversalButton(title_and_search, "View Stock", tester, "black")

# --- The Main Graph

# Setting up where the graph box will be
graph = Frame(window, width = 550, height = 300, background = "grey")

# Placing the graph box
graph.place(relx = 0.5, rely = 0.5, anchor = "center")

# --- Time Buttons

# Creating a frame to hold all the buttons
timebutton_row = Frame(window, width = 550, height = 50, background = "yellow")

# Creating the buttons
day_view = UniversalButton(timebutton_row, "DAY", tester, "black")
week_view = UniversalButton(timebutton_row, "WEEK", tester, "black")
month_view = UniversalButton(timebutton_row, "MONTH", tester, "black")
sixmonth_view = UniversalButton(timebutton_row, "6 MONTH", tester, "black")
year_view = UniversalButton(timebutton_row, "YEAR", tester, "black")
alltime_view = UniversalButton(timebutton_row, "ALL TIME", tester, "black")
companyinfo_view = UniversalButton(timebutton_row, "COMPANY INFO", tester, "black")

# --- Recently Viewed Tab

# Setting up where this tab will be
recentlyviewed = Frame(window, width = 150, height = 300, background = "black")

# Setting up what is within this tab
recentlyviewed_text = UniversalLabel(recentlyviewed, "Recently Viewed", "red")

# --- Stock Info Tab

# Setting up where this tab will be
stockinfo = Frame(window, width = 150, height = 300, background = "black")

# Setting up its mini title
stockinfo_text = UniversalLabel(stockinfo, "Stock Info", "red")

# Setting up the entry field for amount to buy and sell
purchase_entry = Entry(stockinfo, width = 5)

'''
# Putting the input vaildation function for this purchase entry field
purchase_entry_reg = window.register(input_val_num)
purchase_entry.configure(validate = "key",vcmd = (reg,"%P"))
'''

# Setting up the buy and sell buttons
buy_button = UniversalButton(stockinfo, "BUY", tester, "red")
sell_button = UniversalButton(stockinfo, "SELL", tester, "red")

# --- Placing Everything

# Placing the frame for the title and search bar
title_and_search.place(relx = 0.05, rely = 0.1)

# Placing the title of this screen
title.place(relx = 0, rely = 0.5, anchor = "w")

# Placing all that is within the top of screen
searchbar.place(relx = 0.85, rely = 0.5, anchor = "e")
view_button.place(relx = 0.98, rely = 0.5, anchor = "e")

# Placing the button box
timebutton_row.place(relx = 0.5, rely = 0.8, anchor = "center")

# Placing the buttons within the button box frame
day_view.place(relx = 0.12, rely = 0.5, anchor = "center")
week_view.place(relx = 0.24, rely = 0.5, anchor = "center")
month_view.place(relx = 0.38, rely = 0.5, anchor = "center")
sixmonth_view.place(relx = 0.54, rely = 0.5, anchor = "center")
year_view.place(relx = 0.69, rely = 0.5, anchor = "center")
alltime_view.place(relx = 0.84, rely = 0.5, anchor = "center")

# Placing the recently viewed tab
recentlyviewed.place(relx = 0.05, rely = 0.5, anchor = "w")

# Placing all that is within the recently viewed tab
recentlyviewed_text.place(relx = 0.5, rely = 0.05, anchor = "n")

# Placing the stock info tab
stockinfo.place(relx = 0.95, rely = 0.5, anchor = "e")

# Placing all that is within the stock info tab
stockinfo_text.place(relx = 0.5, rely = 0.05, anchor = "n")
purchase_entry.place(relx = 0.5, rely = 0.8, anchor = "s")
buy_button.place(relx = 0.25, rely = 0.95, anchor = "s")
sell_button.place(relx = 0.75, rely = 0.95, anchor = "s")

# When all is done, run the main window
window.mainloop()