


import matplotlib.pyplot as plt




def bar_plotter(ax, datax, datay, **kwargs):
    return ax.bar(datax, datay, **kwargs)


if __name__ == '__main__':
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    datay = [3, 7, 4, 5, 6, 3, 5]
    datax = list(range(1, len(datay)+1))
    print(datay)
    ax1.bar(datax, datay)
    ax1.bar(datax, datay, width=0.5)
    # bar_plotter(ax1, datax, datay)
    plt.show()

