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

# Setting the background to black
window.configure(bg = "black")

# Defining the size of the window using the "geometry" function
# Also restricting if the window can be resized
window.geometry("1000x700")
window.resizable(0, 0)

# --- Classes Within The Program

# Class for buttons within the program
class UniversalButton(Button):
    
    def __init__(self, master, text, command, fg, bg, **kwargs):
        super().__init__(master, text=text, command=command, fg=fg, bg=bg)
        
        self['text'] = text
        self['command'] = command
        self['fg'] = fg
        self['bg'] = bg
        
        self.config(**kwargs)

# Class for labels within the program
class UniversalLabel(Label):
    
    def __init__(self, master, text, fg, bg, **kwargs):
        super().__init__(master, text=text, fg=fg, bg=bg)
        
        self['text'] = text
        self['fg'] = fg
        self['bg'] = bg
        
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

# Setting up where these assets will go
title_and_search = Frame(window, width = 900, height = 100, bg = "black")

# Setting up the text that displays the name of the screen
title = Label(title_and_search, text = "Investment Tracker", bg = "black", fg = "white", font = ("Arial bold", 30))

# Setting up the search bar via an entry field
searchbar = Entry(title_and_search, width = 10)

# Putting the input vaildation function for this search bar
searchbar_reg = window.register(input_val_text)
searchbar.configure(validate = "key",vcmd = (searchbar_reg,"%P"))

# The view button for when the user types into the entry field
view_button = UniversalButton(title_and_search, "View Stock", tester, "black", "white")

# --- The Main Graph

# Setting up where the graph box will be
graph = Frame(window, width = 300, height = 300, background = "grey")

# Placing the graph box
graph.place(relx = 0.5, rely = 0.5, anchor = "center")

# --- Time Buttons

# Creating a frame to hold all the buttons
timebutton_row = Frame(window, width = 550, height = 50, background = "yellow")

# Creating the buttons
day_view = UniversalButton(timebutton_row, "DAY", tester, "black", "yellow")
week_view = UniversalButton(timebutton_row, "WEEK", tester, "black", "yellow")
month_view = UniversalButton(timebutton_row, "MONTH", tester, "black", "yellow")
sixmonth_view = UniversalButton(timebutton_row, "6 MONTH", tester, "black", "yellow")
year_view = UniversalButton(timebutton_row, "YEAR", tester, "black", "yellow")
alltime_view = UniversalButton(timebutton_row, "ALL TIME", tester, "black", "yellow")
companyinfo_view = UniversalButton(timebutton_row, "COMPANY INFO", tester, "black", "yellow")

# --- Recently Viewed Tab

# Setting up where this tab will be
recentlyviewed = Frame(window, width = 150, height = 390, background = "white")

# Setting up what is within this tab
recentlyviewed_text = Label(recentlyviewed, text = "Recently Viewed", fg = "red", bg = "white", font = ("Arial bold", 16))

# The listbox for this tab
recentlyviewed_info = Listbox(recentlyviewed, height = 390)

# Info in the listbox
for i in range(1, 11):
    recentlyviewed_info.insert(END, i)

# Function for selecting an item within the listbox
def listbox_selection():
    for i in recentlyviewed_info.curselection():
        print(recentlyviewed_info.get(i))

# Button for printing a user's selection to the console
select_button = UniversalButton(window, "View Recent", listbox_selection, "black", "black")

# --- Stock Info / Portfolio Tab

# Setting up where this tab will be
stockinfo = Frame(window, width = 150, height = 390, background = "white")

# Setting up its titles
stockinfo_text = Label(stockinfo, text = "Stock Info", fg = "red", bg = "white", font = ("Arial bold", 16))
portfolio_text = Label(stockinfo, text = "User Portfolio", fg = "red", bg = "white", font = ("Arial bold", 16))

# Setting up the entry field for amount to buy and sell
purchase_entry = Entry(stockinfo, width = 5)

# Putting the input vaildation function for this purchase entry field
purchase_entry_reg = window.register(input_val_num)
purchase_entry.configure(validate = "key",vcmd = (purchase_entry_reg,"%P"))

# Setting up the buy and sell buttons
buy_button = UniversalButton(stockinfo, "BUY", tester, "red", "black")
sell_button = UniversalButton(stockinfo, "SELL", tester, "red", "black")

'''
Text label for the price / REMOVE IF NEEDED
price_label = Label(stockinfo, text = "XXX", fg = "black", bg = "white", font = ("Arial", 15))
'''

# --- Quit Button

quit_button = UniversalButton(window, "Quit App", window.quit, "black", "black")

# --- Placing Everything

# Placing the frame for the title and search bar
title_and_search.place(relx = 0.05, rely = 0.1)

# Placing the title of this screen
title.place(relx = 0, rely = 0.5, anchor = "w")

# Placing all that is within the top of screen
searchbar.place(relx = 0.85, rely = 0.5, anchor = "e")
view_button.place(relx = 0.98, rely = 0.5, anchor = "e")

# Placing the button box
timebutton_row.place(relx = 0.5, rely = 0.9, anchor = "center")

# Placing the buttons within the button box frame
day_view.place(relx = 0.12, rely = 0.5, anchor = "center")
week_view.place(relx = 0.24, rely = 0.5, anchor = "center")
month_view.place(relx = 0.38, rely = 0.5, anchor = "center")
sixmonth_view.place(relx = 0.54, rely = 0.5, anchor = "center")
year_view.place(relx = 0.69, rely = 0.5, anchor = "center")
alltime_view.place(relx = 0.84, rely = 0.5, anchor = "center")

# Placing the recently viewed tab
recentlyviewed.place(relx = 0.05, rely = 0.56, anchor = "w")

# Placing all that is within the recently viewed tab
recentlyviewed_text.place(relx = 0.5, rely = 0.05, anchor = "n")
recentlyviewed_info.place(rely = 0.15)
select_button.place(relx = 0.07, rely = 0.85)

# Placing the stock info tab
stockinfo.place(relx = 0.95, rely = 0.56, anchor = "e")

# Placing all that is within the stock info tab
stockinfo_text.place(relx = 0.5, rely = 0.05, anchor = "n")

'''
REMOVE IF NEEDED
price_label.place(relx = 0.5, rely = 0.15, anchor = "n")
'''

purchase_entry.place(relx = 0.5, rely = 0.3, anchor = "s")
buy_button.place(relx = 0.25, rely = 0.4, anchor = "s")
sell_button.place(relx = 0.75, rely = 0.4, anchor = "s")

portfolio_text.place(relx = 0.5, rely = 0.45, anchor = "n")

# Placing the quit button
quit_button.place(relx = 0.83, rely = 0.85)

# When all is done, run the main window
window.mainloop()
