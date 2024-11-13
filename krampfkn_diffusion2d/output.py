import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from numpy import ndarray

def create_plot(data: ndarray, ax: Axes, title: str, boundaries: range) -> AxesImage:
    im = ax.imshow(data.copy(), cmap=plt.get_cmap('hot'), vmin=boundaries.start, vmax=boundaries.stop)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title(title)
    return im

def output_plots(data: [(float, ndarray)], boundaries: range) -> Figure:
    fig_counter = 0
    fig = plt.figure()

    if len(data) == 0:
        return fig

    for (ts,u) in data:
        print(ts, u)
        fig_counter += 1
        ax = fig.add_subplot(220 + fig_counter)
        im = create_plot(u, ax, '{:.1f} ms'.format(ts), boundaries)

    # Plot output figures
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()

    return fig