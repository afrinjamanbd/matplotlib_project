from matplotlib import pyplot as plt
from Core.ABCplot import ABCTest


class StackPlot(ABCTest):
    def __init__(self, arr, labels):
        self.arr = arr
        self.label_list = labels

    def set_title(self, title):
        super().set_title(title)

    def xy_title(self, x_title, y_title):
        pass

    def add(self):
        plt.stackplot(self.arr, labels=self.label_list)

    def add_new(self, a, b, num, label):
        pass

    def show(self):
        plt.tight_layout()
        plt.legend()
        plt.show()



