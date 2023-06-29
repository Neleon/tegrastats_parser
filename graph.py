import csv
import matplotlib.pyplot as plt
import pandas as pd
import random

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange',
          'purple', 'brown', 'gray', 'cyan', 'magenta']

pairs = [('Time (mS)', 'Used RAM (MB)'),
         ('Time (mS)', 'Total RAM (MB)'),
         ('Time (mS)', 'Number of Free RAM Blocks'),
         ('Time (mS)', 'Size of Free RAM Blocks (MB)'),
         ('Time (mS)', 'CPU Frequency (MHz)'),
         ('Time (mS)', 'CPU 0 Load (%)'),
         ('Time (mS)', 'CPU 1 Load (%)'),
         ('Time (mS)', 'CPU 2 Load (%)'),
         ('Time (mS)', 'CPU 3 Load (%)'),
         ('Time (mS)', 'CPU 4 Load (%)'),
         ('Time (mS)', 'CPU 5 Load (%)'),
         ('Time (mS)', 'CPU 6 Load (%)'),
         ('Time (mS)', 'CPU 7 Load (%)'),
         ('Time (mS)', 'CPU 8 Load (%)'),
         ('Time (mS)', 'CPU 9 Load (%)'),
         ('Time (mS)', 'CPU 10 Load (%)'),
         ('Time (mS)', 'CPU 11 Load (%)'),
         ('Time (mS)', 'APE frequency (MHz)'),
         ('Time (mS)', 'Used GR3D (%)'),
         ('Time (mS)', 'GR3D Frequency (MHz)'),
         ('Time (mS)', ' Temperature (C)'),
         ('Time (mS)', 'CPU Temperature (C)'),
         ('Time (mS)', 'GPU Temperature (C)'),
         ('Time (mS)', 'tj Temperature (C)')]

class Graph:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, skiprows=0, header=0, index_col=0)

    def scatter_plot(self, x, y):
        # plt.rcParams['figure.max_open_warning'] = 50 # can be removed because of add plt.close()
        plt.figure()
        plt.title(f'{x} vs. {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        # plt.scatter(self.df.loc[:, x], self.df.loc[:, y]) # scatter
        plt.plot(self.df.loc[:, x], self.df.loc[:, y], color=colors[random.randint(0, 100) % len(colors)]) # plot
        # plt.savefig(f'{x} vs. {y}.png')
        plt.show()
        plt.close()

    def plots(self):
        for pair in pairs:
            if pair[1] in self.df.columns:
                self.scatter_plot(pair[0], pair[1])
            else:
                print('warning: the key: "{}" not exists'.format(pair[1]))

if __name__ == '__main__':
    csv_file = 'sample_log.csv'

    graph = Graph(csv_file)
    graph.plots()
