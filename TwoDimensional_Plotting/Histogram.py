from matplotlib import pyplot as plt
from Core.ABCplot import ABCTest


class Histogram(ABCTest):

    log = False
    def __init__(self, x, bins, log):
        self.x = x
        self.bins = bins
        self.log = log

    def add(self):
        return plt.hist(self.x, bins=self.bins, edgecolor=self.color, log=self.log)

    def add_new(self, x, bins, log):
        return plt.hist(self.x, bins=bins, edgecolor=self.color, log=log)

    def add_median(self, median, color, label):
        return plt.axvline(median, color, label=label) #Need to fix

    def set_title(self, title):
        super().set_title(title)

    def xy_title(self, x_title, y_title):
        super().xy_title(x_title, y_title)

    def show(self):
        super().show()
