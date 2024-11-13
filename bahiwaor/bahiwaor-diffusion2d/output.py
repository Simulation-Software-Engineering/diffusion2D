import matplotlib.pyplot as plt

def create_plot(u, T_cold, T_hot, dt, timestep, fig, position):
    """
    Creates a single plot for a given timestep.
    
    Parameters:
    - u: 2D numpy array, temperature distribution at the current timestep
    - T_cold: float, cold temperature of the domain
    - T_hot: float, hot temperature in the center
    - dt: float, time step size
    - timestep: int, current timestep number
    - fig: matplotlib Figure object
    - position: int, subplot position within the figure
    """
    ax = fig.add_subplot(position)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(timestep * dt * 1000))
    return im

def output_plots(fig, im):
    """
    Finalizes the plotting by adding a color bar and showing the figure.
    
    Parameters:
    - fig: matplotlib Figure object containing all subplots
    - im: AxesImage object for the color bar reference
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()
