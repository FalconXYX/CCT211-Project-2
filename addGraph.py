from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) # the figure that will contain the plot 
import stockAPI
import createGraph




def hour(ticker: str, window, name: str ):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getLastHourData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price Last Hour')
    g.formatDatesLong(15)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas

def day(ticker: str, window, name: str):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getLastDayData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price Last Day')
    g.formatDatesLong(15)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas

def week(ticker: str, window, name: str):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getLastWeekData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price Last Week')
    g.formatDatesLong(15)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas

def month(ticker: str, window, name: str):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getLastMonthData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price Last Month')
    g.formatDatesLong(10)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas

def sixMonth(ticker: str, window, name: str):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getLast6MonthData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price Last 6 Months')
    g.formatDatesLong(10)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas

def year(ticker: str, window, name: str):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getLastYearData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price Last Year')
    g.formatDatesLong(15)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas

def alltime(ticker: str, window, name: str):
    stock = stockAPI.Stock(ticker)
    d,dd = stock.getAllTimeData()
    g = createGraph.Graph(dd,d)
    g.label('Time','Price',name+' Stock Price All Time')
    g.formatDatesLong(15)
    g.plot()
    fig = g.show()
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 
    return canvas