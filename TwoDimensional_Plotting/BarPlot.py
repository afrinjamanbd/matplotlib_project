from matplotlib import pyplot as plt
from Core.ABCplot import ABCTest


class BarChart(ABCTest):
    # print(plt.style.available)

    def __init__(self, x, y, color, label):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

    def add(self):
        return plt.bar(self.x - self.width, self.y, self.width, label=self.label, color=self.color)

    def add_new(self, a, b, num, label):
        return plt.bar(a + self.width * num, b, self.width, color=self.color, label=label)

    def set_title(self, title):
        super().set_title(title)

    def xy_title(self, x_title, y_title):
        super().xy_title(x_title, y_title)

    def show(self):
        plt.style.use("fivethirtyeight")
        super().show()
