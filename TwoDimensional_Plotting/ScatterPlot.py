from matplotlib import pyplot as plt
from Core.ABCplot import ABCTest

class ScatterPlot(ABCTest):
    log = False
    line_width = 1
    color = 'black'
    alpha = 0.75
    size = 50

    def __init__(self, x, y, log):
        self.x = x
        self.y = y
        self.log = log

    def add(self):
        plt.scatter(self.x, self.y, s=self.size, edgecolor=self.color, linewidth=self.line_width, alpha=self.alpha)
        if self.log == True:
            plt.xscale('log')
            plt.yscale('log')

    def add_new(self, x, y, log):
        plt.scatter(self.x, self.y, s=self.size, edgecolor=self.color, linewidth=self.line_width, alpha=self.alpha)
        if self.log == True:
            plt.xscale('log')
            plt.yscale('log')

    def set_title(self, title):
        super().set_title(title)

    def xy_title(self, x_title, y_title):
        super().xy_title(x_title, y_title)

    def show(self):
        plt.style.use('seaborn')
        super().show()