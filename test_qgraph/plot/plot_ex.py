import matplotlib.pyplot as plt

def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out


data1 = [1, 2, 3]
data2 = [4, 7, 2]

data3 = [5, 6, 7]
data4 = [4, 5, 3]

fig, ax = plt.subplots(111)
my_plotter(ax, data1, data2, {'marker':'x'})
my_plotter(ax, data3, data4, {'marker':'x'})
plt.show()