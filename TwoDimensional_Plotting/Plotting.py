from matplotlib import pyplot as plt
from Core.ABCplot import ABCTest


class Plotting(ABCTest):

    def __init__(self, x, y, color, label):
        self.x = x
        self.y = y
        self.color = color
        self.label = label

    def add(self):
        plt.plot(self.x, self.y, color=self.color, label=self.label, linewidth=self.line_width, marker=self.marker,
                 linestyle=self.line_style)

    def add_new(self, a, b, num, label):
        plt.plot(a, b, color=self.color, label=label, linewidth=self.line_width, marker=self.marker,
                 linestyle=self.line_style)

    def set_title(self, title):
        super().set_title(title)

    def xy_title(self, x_title, y_title):
        super().xy_title(x_title, y_title)

    def show(self):
        super().show()
