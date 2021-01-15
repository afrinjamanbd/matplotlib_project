from matplotlib import pyplot as plt

class SubPlot:
    fig, ax = plt.subplots()
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def add (self, label1, label2, label3):
        ax1.plot(x, w, color='#444444', linestyle='--', label=label3)
        ax2.plot(x, y, label1)
        ax2.plot(x, z, label2)


    def title(self, title, x_label, y_label):
        ax1.set_title(title)
        ax1.set_xlabel(x_label)
        ax1.set_ylabel(y_label)
        ax2.set_title(title)
        ax2.set_xlabel(x_label)
        ax2.set_ylabel(y_label)

    def show(self):
        ax1.lagend()
        ax2.lagend()
        plt.tight_layout
        plt.show()
