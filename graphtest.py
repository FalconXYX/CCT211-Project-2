#DO NOT USE THIS FOR THE MAIN CODE THIS ID FOR TESTING AND EXAMPLE ONLY


from tkinter import *
import addGraph
# plot function is created for 
# plotting the graph in 
# tkinter window 
def plot(window): 
	canvas = addGraph.day("AAPL", window, "Apple")
	canvas.get_tk_widget().pack() 

# the main Tkinter window 
window = Tk() 

# setting the title 
window.title('Plotting in Tkinter') 

# dimensions of the main window 
window.geometry("600x600") 

# button that displays the plot 
plot_button = Button(master = window, 
					command = lambda: plot(window), 
					height = 2, 
					width = 10, 
					text = "Plot") 

# place the button 
# in main window 
plot_button.pack() 

# run the gui 
window.mainloop() 
