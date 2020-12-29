from matplotlib import pyplot as plt
from Core.ABCplot import ABCTest


class PieChart(ABCTest):

    # explode has to be like explode = [0.1, 0, 0, 0, 0, 0]
    explode = None

    # shadow is a boolean value
    shadow = True

    # startangle has to be within 360 degree
    startangle = 80

    # autopct is a value like autopct='%1.1f%%'
    autopct = None

    # edge color of pie chart
    edgecolor = '#D9E248'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        plt.pie(self.x, labels=self.y, explode=self.explode, shadow=self.shadow, startangle=self.startangle,
                autopct=self.autopct, wedgeprops={'edgecolor': self.edgecolor})

    def add_new(self, a, b, num, label):
        pass

    def set_title(self, title):
        super().set_title(title)

    def xy_title(self, x_title, y_title):
        pass

    def show(self):
        plt.tight_layout()
        plt.show()
