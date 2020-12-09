from matplotlib import pyplot as plt


class SimpleBarChart:
    width = .25

    def __init__(self, title_x, title_y, fig_title):
        self.title_x = title_x
        self.title_y = title_y
        self.fig_title = fig_title

    def bar(self, x, y, z):

        plt.barh(x, y, label='x and y')
        plt.barh(x, z, label='x and z')
        plt.style.use("fivethirtyeight")
        # print(plt.style.available)
        plt.title(self.fig_title)
        plt.xlabel(self.title_x)
        plt.ylabel(self.title_y)
        plt.tight_layout()
        plt.legend()
        plt.grid(True)
        plt.show()


class SimplePlotting:

    def __init__(self, title_x, title_y, fig_title):
        self.title_x = title_x
        self.title_y = title_y
        self.fig_title = fig_title

    def plots(self, x, y, z):
        plt.plot(x, y, color='#444444', label='x and y', linewidth=.3)
        plt.plot(x, z, color='#008fd5', label='x and z', linewidth=.5, marker='.', linestyle='--')
        plt.title(self.fig_title)
        plt.xlabel(self.title_x)
        plt.ylabel(self.title_y)
        plt.tight_layout()
        plt.legend()
        plt.grid(True)
        plt.show()


class SimplePieChart:

    def __init__(self, title):
        self.title = title

    def piecharts(self, x, y, explode):
        plt.pie(x, labels=y, explode=explode, shadow=True, startangle=80, autopct='%1.1f%%', wedgeprops={'edgecolor': '#444444'})
        plt.tight_layout()
        plt.title(self.title)
        plt.show()

    def stackplotting(self, x, p, q, r, s, t, labels):
        plt.stackplot(x, p, q, r, s, t, labels=labels)
        plt.title(self.title)
        plt.tight_layout()
        plt.legend()
        plt.show()


