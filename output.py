import matplotlib.pyplot as plt


def create_plot(fig_counter, fig, u, T_cold, T_hot, n, dt):
    """Create one plot for a particular time stamp

    Keyword arguments:
    fig_counter -- counter for the subfigure
    fig -- matplotlib figure object
    u -- matrix of temperature values
    T_cold -- value representing cold temperature
    T_hot -- value representing hot temperature
    n -- value for timestep
    dt -- stable timestamp value
    """
    ax = fig.add_subplot(220 + fig_counter)
    im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
    ax.set_axis_off()
    ax.set_title('{:.1f} ms'.format(n * dt * 1000))
    return fig, im


def output_plots(fig, im):
    """Outputs all the plots as one figure
    
    Keyword arguments:
    fig -- matplotlib figure object
    im -- image for color bar axes
    """
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
    cbar_ax.set_xlabel('$T$ / K', labelpad=20)
    fig.colorbar(im, cax=cbar_ax)
    plt.show()