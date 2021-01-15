from abc import ABC, abstractmethod
from matplotlib import pyplot as plt


# Abstract Class for Plotting
class ABCTest(ABC):
    width = .25
    color = None
    label = None
    marker = None
    line_width = None
    line_style = None
    theme = plt.axes().set_facecolor('#EDF1DB')

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def add_new(self, a, b, num, label):
        pass

    def set_title(self, title):
        plt.title(title)

    def xy_title(self, x_title, y_title):
        if (x_title is not None) and (y_title is not None):
            plt.xlabel(x_title)
            plt.ylabel(y_title)
        elif (x_title is not None) and (y_title is None):
            plt.xlabel(x_title)
        elif (x_title is None) and (y_title is not None):
            plt.ylabel(y_title)
        else:
            pass

    @abstractmethod
    def show(self):
        plt.tight_layout()
        plt.grid(True)
        plt.legend()
        plt.show()

