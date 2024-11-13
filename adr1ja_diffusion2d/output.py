import matplotlib.pyplot as plt

def create_plot(u, T_cold, T_hot, dt, n, fig, fig_counter):
    """Creates a single plot for a given time step."""
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return im  # return the image for color bar usage later

def output_plots(im, fig):
    """Combines plots into a single figure and displays the color bar."""
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
