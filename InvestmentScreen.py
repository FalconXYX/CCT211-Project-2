"""
CCT211 Project 2: Investment Screen
"""

# Import tkinter and its functions
import tkinter 
from tkinter import *


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

class InvestmentScreenClass():
    def __init__(self, window, acount):
        self.w = window
        self.window = tkinter.Frame(self.w)
        self.window.configure(bg="black")
        self.acount = acount
        self.stockinfo = Frame(window, width = 150, height = 390, background = "white")

        # Setting up its titles
        self.stockinfo_text = Label(self.stockinfo, text = "Stock Info", fg = "red", bg = "white", font = ("Arial bold", 16))
        self.portfolio_text = Label(self.stockinfo, text = "User Portfolio", fg = "red", bg = "white", font = ("Arial bold", 16))

        # Setting up the entry field for amount to buy and sell
        self.purchase_entry = Entry(self.stockinfo, width = 5)

        # Putting the input vaildation function for this purchase entry field
        self.purchase_entry_reg = window.register(self.input_val_num)
        self.purchase_entry.configure(validate = "key",vcmd = (self.purchase_entry_reg,"%P"))

        # Setting up the buy and sell buttons
        self.buy_button = UniversalButton(self.stockinfo, "BUY", tester, "red", "black")
        self.sell_button = UniversalButton(self.stockinfo, "SELL", tester, "red", "black")

        '''
        Text label for the price / REMOVE IF NEEDED
        price_label = Label(stockinfo, text = "XXX", fg = "black", bg = "white", font = ("Arial", 15))
        '''
        self.quit_button = UniversalButton(window, "Quit App", window.quit, "black", "black")
        self.title_and_search = Frame(window, width = 900, height = 100, bg = "black")

        # Setting up the text that displays the name of the screen
        self.title = Label(self.title_and_search, text = "Investment Tracker", bg = "black", fg = "white", font = ("Arial bold", 30))

        # Setting up the search bar via an entry field
        self.searchbar = Entry(self.title_and_search, width = 10)

        # Putting the input vaildation function for this search bar
        self.searchbar_reg = window.register(self.input_val_text)
        self.searchbar.configure(validate = "key",vcmd = (self.searchbar_reg,"%P"))

        # The view button for when the user types into the entry field
        self.view_button = UniversalButton(self.title_and_search, "View Stock", tester, "black", "white")

        # --- The Main Graph

        # Setting up where the graph box will be
        self.graph = Frame(window, width = 300, height = 300, background = "grey")

        # --- Time Buttons

        # Creating a frame to hold all the buttons
        self.timebutton_row = Frame(window, width = 550, height = 50, background = "yellow")

        # Creating the buttons
        self.day_view = UniversalButton(self.timebutton_row, "DAY", tester, "black", "yellow")
        self.week_view = UniversalButton(self.timebutton_row, "WEEK", tester, "black", "yellow")
        self.month_view = UniversalButton(self.timebutton_row, "MONTH", tester, "black", "yellow")
        self.sixmonth_view = UniversalButton(self.timebutton_row, "6 MONTH", tester, "black", "yellow")
        self.year_view = UniversalButton(self.timebutton_row, "YEAR", tester, "black", "yellow")
        self.alltime_view = UniversalButton(self.timebutton_row, "ALL TIME", tester, "black", "yellow")
        self.companyinfo_view = UniversalButton(self.timebutton_row, "COMPANY INFO", tester, "black", "yellow")

        # --- Recently Viewed Tab

        # Setting up where this tab will be
        self.recentlyviewed = Frame(window, width = 150, height = 390, background = "white")

        # Setting up what is within this tab
        self.recentlyviewed_text = Label(self.recentlyviewed, text = "Recently Viewed", fg = "red", bg = "white", font = ("Arial bold", 16))

        # The listbox for this tab
        self.recentlyviewed_info = Listbox(self.recentlyviewed, height = 390)
        self.select_button = UniversalButton(window, "View Recent", self.listbox_selection, "black", "black")



    def input_val_text(self,inp):
        if inp.isalpha():
            return True
        
        elif inp == "":
            return True
        
        else:
            return False

    # Input vaildation function for number only
    def input_val_num(self,inp):
        if inp.isnumeric():
            return True
        
        elif inp == "":
            return True
        
        else:
            return False


    # Function for selecting an item within the listbox
    def listbox_selection(self):
        for i in self.recentlyviewed_info.curselection():
            print(self.recentlyviewed_info.get(i))

    def drawWidgets(self):
        self.window.update()
        self.window.update_idletasks()
        self.window.pack(fill="both", expand=True)
        self.graph.place(relx = 0.5, rely = 0.5, anchor = "center")

        # Placing the frame for the title and search bar
        self.title_and_search.place(relx = 0.05, rely = 0.1)

        # Placing the title of this screen
        self.title.place(relx = 0, rely = 0.5, anchor = "w")

        # Placing all that is within the top of screen
        self.searchbar.place(relx = 0.85, rely = 0.5, anchor = "e")
        self.view_button.place(relx = 0.98, rely = 0.5, anchor = "e")

        # Placing the button box
        self.timebutton_row.place(relx = 0.5, rely = 0.9, anchor = "center")

        # Placing the buttons within the button box frame
        self.day_view.place(relx = 0.12, rely = 0.5, anchor = "center")
        self.week_view.place(relx = 0.24, rely = 0.5, anchor = "center")
        self.month_view.place(relx = 0.38, rely = 0.5, anchor = "center")
        self.sixmonth_view.place(relx = 0.54, rely = 0.5, anchor = "center")
        self.year_view.place(relx = 0.69, rely = 0.5, anchor = "center")
        self.alltime_view.place(relx = 0.84, rely = 0.5, anchor = "center")

        # Placing the recently viewed tab
        self.recentlyviewed.place(relx = 0.05, rely = 0.56, anchor = "w")

        # Placing all that is within the recently viewed tab
        self.recentlyviewed_text.place(relx = 0.5, rely = 0.05, anchor = "n")
        self.recentlyviewed_info.place(rely = 0.15)
        self.select_button.place(relx = 0.07, rely = 0.85)

        # Placing the stock info tab
        self.stockinfo.place(relx = 0.95, rely = 0.56, anchor = "e")

        # Placing all that is within the stock info tab
        self.stockinfo_text.place(relx = 0.5, rely = 0.05, anchor = "n")

        '''
        REMOVE IF NEEDED
        price_label.place(relx = 0.5, rely = 0.15, anchor = "n")
        '''

        self.purchase_entry.place(relx = 0.5, rely = 0.3, anchor = "s")
        self.buy_button.place(relx = 0.25, rely = 0.4, anchor = "s")
        self.sell_button.place(relx = 0.75, rely = 0.4, anchor = "s")

        self.portfolio_text.place(relx = 0.5, rely = 0.45, anchor = "n")

        # Placing the quit button
        self.quit_button.place(relx = 0.83, rely = 0.85)
                

def tester():
    print("This is a test, and it has worked")

