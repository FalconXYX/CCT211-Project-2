from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import addGraph
# plot function is created for 
# plotting the graph in 
# tkinter window 
def plot(window): 

	
	canvas = addGraph.hour("AAPL", window, "Apple")
	canvas.get_tk_widget().pack() 


	# placing the toolbar on the Tkinter window 

# the main Tkinter window 
window = Tk() 

# setting the title 
window.title('Plotting in Tkinter') 

# dimensions of the main window 
window.geometry("500x500") 

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
