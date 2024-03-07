import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
class Graph:
    def __init__(self, dataList: list, dateList: list):
        self.dataList = dataList
        self.dateList = dateList
        self.titlefont = {'family': 'serif','color':  'black','weight': 'normal','size': 18}
        self.labelfont = {'family': 'serif','color':  'black','weight': 'normal','size': 12}
        self.fig = Figure(figsize = (6, 6), dpi = 100) 
        self.graph = self.fig.add_subplot(111)  

    def plot(self):
        self.graph.plot(self.dateList, self.dataList,':k')
    def show(self):
        self.fig.tight_layout()
        return self.fig
    def label(self, xlabel: str, ylabel: str, title: str):
        self.graph.set_xlabel(xlabel, fontdict = self.labelfont)
        self.graph.set_ylabel(ylabel, fontdict = self.labelfont)
        self.graph.set_title(title, fontdict = self.titlefont,loc = 'left')
       
 
    def formatDatesLong(self, y):
        times = self.dateList
        n =  max(1, int(len(times) / y))
        
        displayed_labels = [label if index % n == 0 else '' for index, label in enumerate(times)]
        self.graph.set_xticks(ticks=range(len(times)), labels=displayed_labels, rotation=60) # Rotate labels for better readability

