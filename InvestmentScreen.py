"""
CCT211 Project 2: Investment Screen
"""

# Import tkinter and its functions
# Also adding all functions from the repo
import tkinter 
from tkinter import *
from tkinter import messagebox
import acountManagement
import acount
import time
import addGraph
import stockAPI

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

# The class for this window
# Will be used later in the "main" file to draw this screen as a frame
class InvestmentScreenClass():
    def __init__(self, window, acount):
        self.w = window
        self.window = tkinter.Frame(self.w)
        self.window.configure(bg="black")
        self.acount = acount

        # The frame that will hold the graph
        self.stockinfo = Frame(self.window, width = 150, height = 390, background = "white")
        
        # Setting up its titles
        self.stockinfo_text = Label(self.stockinfo, text = "Stock Info", fg = "red", bg = "white", font = ("Arial bold", 16))
        self.portfolio_text = Label(self.stockinfo, text = "User Portfolio", fg = "red", bg = "white", font = ("Arial bold", 16))

        # Labels used for the graph
        self.stockamount = Label(self.stockinfo, text = "Shares Owned", fg = "black", bg = "white", font = ("Arial bold", 10))
        self.stocknetworth_text = Label(self.stockinfo, text = "Net Worth", fg = "black", bg = "white", font = ("Arial bold", 10))
        self.stockpurchase_text = Label(self.stockinfo, text = "Buy Price", fg = "black", bg = "white", font = ("Arial bold", 10))

        self.networth_text = Label(self.stockinfo, text = "Net Worth", fg = "black", bg = "white", font = ("Arial bold", 10))
        self.purchase_text = Label(self.stockinfo, text = "Buy Price", fg = "black", bg = "white", font = ("Arial bold", 10))

        # Setting up the entry field for amount to buy and sell
        self.purchase_entry = Entry(self.stockinfo, width = 5)

        # Putting the input vaildation function for the purchase entry field
        self.purchase_entry_reg = self.window.register(self.input_val_num)
        self.purchase_entry.configure(validate = "key",vcmd = (self.purchase_entry_reg,"%P"))

        # Setting up the buy and sell buttons
        self.buy_button = UniversalButton(self.stockinfo, "BUY", self.buyStock, "red", "black")
        self.sell_button = UniversalButton(self.stockinfo, "SELL", self.sellStock, "red", "black")

        # The label that holds the price of the currently searched stock
        self.price_label = Label(self.stockinfo, text = "", fg = "black", bg = "white", font = ("Arial", 15))

        # The button for quitting the application
        self.quit_button = UniversalButton(self.window, "Quit App", self.quit, "white", "black")

        # --- The Top Part of the Window

        # The frame for holding the window's title and the stock search bar
        self.title_and_search = Frame(self.window, width = 900, height = 100, bg = "black")

        # Setting up the text that displays the name of the screen
        self.title = Label(self.title_and_search, text = "Investment Tracker", bg = "black", fg = "white", font = ("Arial bold", 30))

        # Setting up the search bar via an entry field
        self.searchbar = Entry(self.title_and_search, width = 10)

        # Putting the input vaildation function for this search bar
        self.searchbar_reg = window.register(self.input_val_text)
        self.searchbar.configure(validate = "key",vcmd = (self.searchbar_reg,"%P"))

        # The view button for when the user types into the entry field
        self.view_button = UniversalButton(self.title_and_search, "View Stock", self.addStock, "black", "white")

        # --- The Main Graph

        # Setting up where the graph box will be
        self.graph = Frame(window, width = 300, height = 300, background = "grey")

        # --- Time Buttons

        # Creating a frame to hold all the buttons
        self.timebutton_row = Frame(self.window, width = 550, height = 50, background = "yellow")

        # Creating the buttons
        self.day_view = UniversalButton(self.timebutton_row, "DAY",lambda: self.updateGraph("DAY"), "black", "yellow",)
        self.week_view = UniversalButton(self.timebutton_row, "WEEK",lambda: self.updateGraph("WEEK"), "black", "yellow",)
        self.month_view = UniversalButton(self.timebutton_row, "MONTH",lambda: self.updateGraph("MONTH"), "black", "yellow")
        self.sixmonth_view = UniversalButton(self.timebutton_row, "6 MONTH", lambda: self.updateGraph("SIXMONTH"),"black", "yellow")
        self.year_view = UniversalButton(self.timebutton_row, "YEAR",lambda: self.updateGraph("YEAR"), "black", "yellow",)
        self.alltime_view = UniversalButton(self.timebutton_row, "ALL TIME",lambda: self.updateGraph("ALLTIME"), "black", "yellow")
        self.companyinfo_view = UniversalButton(self.timebutton_row, "COMPANY INFO", lambda: self.updateGraph("COMPANYINFO"),"black", "yellow", )

        # --- Recently Viewed Tab

        # Setting up where this tab will be
        self.recentlyviewed = Frame(self.window, width = 150, height = 390, background = "white")

        # Setting up what is within this tab
        self.recentlyviewed_text = Label(self.recentlyviewed, text = "Recently Viewed", fg = "red", bg = "white", font = ("Arial bold", 16))

        # The listbox for this tab
        self.recentlyviewed_info = Listbox(self.recentlyviewed, height = 390)
        self.select_button = UniversalButton(self.window, "Select Stock", self.listbox_selection, "white", "black")
        self.addItems()

    # The function that updates data such as recently viewed stocks and any purchases
    # Occurs when the user quits the application
    def quit(self):
        self.acount.updateFile()
        self.w.quit()

    # The function to grab the stock that the user has searched for
    # To ensure minimal errors, the search is set to be in all upper case letters
    def addStock(self):
        symbol = self.searchbar.get()
        symbol = symbol.upper()
        stock = stockAPI.Stock(symbol)

        try:
            self.acount.addStock(symbol, stock.getName(), 0, 0)
            self.currentStock = self.acount.getStock(symbol)
            
        # If the stock search is invaild, a message box appears
        except:
            
            messagebox.showerror("", "Invaild Stock Name")
            return
        self.addItems()
        self.updateStockInfo()

    # The function for buying stocks
    def buyStock(self):
        amount = self.purchase_entry.get()
        if(amount == ""):
            messagebox.showerror("Please Try Again", "Invaild Buying Amount")
            return
        self.acount.updateStock(self.currentStock.symbol, int(amount), self.currentStock.getCurrentPrice())
        self.updateStockInfo()

    # The function for selling stocks
    def sellStock(self):
        amount = self.purchase_entry.get()
        if(amount == ""):
            messagebox.showerror("Please Try Again", "Invaild Buying Amount")
            return
        status = self.acount.updateStock(self.currentStock.symbol, -int(amount), self.currentStock.getCurrentPrice())
        if status == False:
            messagebox.showerror("Please Try Again", "Invaild Selling Amount")
            return
        self.updateStockInfo()

    # The function that adds any searched stocks into the Recently Viewed tab
    def addItems(self):
        self.recentlyviewed_info.delete(0,END)
        num = 1
        for stock in self.acount.stocks:
            if num ==1:
                self.currentStock = self.acount.stocks[0]
            self.recentlyviewed_info.insert(num,stock.symbol)
            num+=1

    # Input vaildation function for text only
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

    # The function that updates the graph based on the selected time buttons along the bottom of the window
    def updateGraph(self, time):
        try:
            self.g.get_tk_widget().pack_forget()

        except:
            pass
        if(time == "HOUR"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.hour(self.currentStock.symbol,self.graph,stock.getName())
        if(time == "DAY"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.day(self.currentStock.symbol,self.graph,stock.getName())
        if(time == "WEEK"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.week(self.currentStock.symbol,self.graph,stock.getName())
        if(time == "MONTH"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.month(self.currentStock.symbol,self.graph,stock.getName())
        if(time == "SIXMONTH"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.sixMonth(self.currentStock.symbol,self.graph,stock.getName())
        if(time == "YEAR"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.year(self.currentStock.symbol,self.graph,stock.getName())
        if(time == "ALLTIME"):
            s = self.currentStock.symbol
            stock = stockAPI.Stock(s)
            self.g = addGraph.alltime(self.currentStock.symbol,self.graph,stock.getName())

        self.g.get_tk_widget().pack()


    # Function for selecting an item within the listbox
    def listbox_selection(self):
        for i in self.recentlyviewed_info.curselection():
            st = self.recentlyviewed_info.get(i)
            self.currentStock = self.acount.getStock(st)
            self.updateStockInfo()
            self.updateGraph("HOUR")

    # The function that displays information about the currently searched for stock   
    def updateStockInfo(self):
        self.stockinfo_text['text'] = "Stock Info: " + self.currentStock.symbol
        self.price_label['text'] = "Price: " + str(self.currentStock.getCurrentPrice())
        self.purchase_entry.delete(0,END)
        self.acount.updateNetWorth()
        self.acount.updateTotalInvested()
        self.purchase_text['text'] = "Buy Price: " + str(round(self.acount.totalInvested))
        self.networth_text['text'] = "Net Worth: " + str(round(self.acount.netWorth))
        self.stockamount['text'] = "Shares Owned: " + str(self.currentStock.shares)
        self.stocknetworth_text['text'] = "Net Worth: " + str(round(self.currentStock.getCurrentPrice() * self.currentStock.shares))
        self.stockpurchase_text['text'] = "Buy Price: " + str(round(self.currentStock.purchasePrice * self.currentStock.shares))


    # Finally, all widgets are drawn onto the window using the place method
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

        
        self.price_label.place(relx = 0.5, rely = 0.15, anchor = "n")
        
        # Placing the stock purchase bar, as well as the buy and sell buttons
        self.purchase_entry.place(relx = 0.5, rely = 0.3, anchor = "s")
        self.buy_button.place(relx = 0.25, rely = 0.4, anchor = "s")
        self.sell_button.place(relx = 0.75, rely = 0.4, anchor = "s")

        self.stockamount.place(relx = 0.5, rely = 0.45, anchor = "center")
        self.stocknetworth_text.place(relx = 0.5, rely = 0.5, anchor = "center")
        self.stockpurchase_text.place(relx = 0.5, rely = 0.55, anchor = "center")

        self.portfolio_text.place(relx = 0.5, rely = 0.6, anchor = "n")

        
        self.networth_text.place(relx = 0.5, rely = 0.7, anchor = "center")
        self.purchase_text.place(relx = 0.5, rely = 0.75, anchor = "center")


        # Placing the quit button
        self.quit_button.place(relx = 0.83, rely = 0.85)

