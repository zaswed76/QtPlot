import matplotlib.pyplot as plt
from enum import Enum





class Axis:
    OneAxis = "one_axis"
    Two_axis = "two_axis"
    Three_axis = "three_axis"
    Four_axis = "four_axis"
    name_num = {1: OneAxis, 2: Two_axis, 3: Three_axis, 4: Four_axis}


    def __init__(self, figure):
        self.figure = figure

    def __call__(self, name, **kwargs):
        if isinstance(name, str):
            return getattr(Axis, name)(self, **kwargs)
        elif isinstance(name, int):
            try:
                axs = getattr(Axis, self.name_num[name])(self, **kwargs)
            except KeyError:
                raise Exception("график с таким колличестом осей не определён")
            else:
                return axs

    def one_axis(self, **kwargs):
        return (self.figure.add_subplot(111),)

    def two_axis(self, **kwargs):
        a = self.figure.add_subplot(211)
        a.tick_params(axis='x', labelbottom='off', bottom=False)
        b = self.figure.add_subplot(212)
        plt.tight_layout(h_pad=2, pad=1)
        return a, b

    def four_axis(self, **kwargs):
        ax1 = self.figure.add_subplot(221)
        ax2 = self.figure.add_subplot(222)
        ax3 = self.figure.add_subplot(223)
        ax4 = self.figure.add_subplot(224)
        ax1.tick_params(axis='x', labelbottom='off', bottom=False)
        ax2.tick_params(axis='x', labelbottom='off', bottom=False)
        ax2.tick_params(axis='y', labelleft='off', left=False)
        ax4.tick_params(axis='y', labelleft='off', left=False)
        plt.tight_layout(h_pad=-0.1, w_pad=-0.1, pad=1)
        return ax1, ax2, ax3, ax4

    def three_axis(self, **kwargs):
        ax1 = self.figure.add_subplot(221)
        ax3 = self.figure.add_subplot(223)
        ax4 = self.figure.add_subplot(224)
        ax1.tick_params(axis='x', labelbottom='off', bottom=False, color="red")
        ax4.tick_params(axis='y', labelleft='off', left=False)
        plt.tight_layout(h_pad=-0.1, w_pad=-0.1, pad=1)
        return ax1, ax3, ax4,

    def set_grid(self, vline=False, hline=False, **kwargs):
        for ax in self.figure.axes:
            if vline:
                ax.xaxis.grid(**kwargs)
            if hline:
                ax.yaxis.grid(**kwargs)

    def grid(self, v: bool):
        for ax in self.figure.axes:
            ax.grid(v)


if __name__ == '__main__':
    from test_qgraph.plot import plot_rc

    plot_rc.first_param()
    fig = plt.figure()
    axis = Axis(fig)

    axs = axis(3)
    for ax in axs:
        ax.bar([1, 2, 3], [1, 2, 3])
    plt.show()
