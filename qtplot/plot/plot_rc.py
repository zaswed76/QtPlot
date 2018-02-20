import matplotlib.pyplot as plt

def first_param():
    plt.rcParams['grid.color'] = "grey"
    plt.rcParams['grid.alpha'] = 0.5
    plt.rcParams['grid.linewidth'] = 0.4
    plt.rcParams['grid.linestyle'] = "--"
    plt.rcParams['xtick.color'] = "b"
    plt.rcParams['xtick.labelsize'] = 8


def second_param():
    plt.rcParams['grid.color'] = "grey"
    plt.rcParams['grid.alpha'] = 0.5
    plt.rcParams['grid.linewidth'] = 0.4
    plt.rcParams['grid.linestyle'] = ":"
    plt.rcParams['xtick.color'] = "b"