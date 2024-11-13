import numpy as np
import matplotlib.pyplot as plt
from output import create_plot, output_plots

def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    # Propagate with forward-difference in time, central-difference in space
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
            (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
            + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)
    u_nm1 = u.copy()
    return u_nm1, u

def solve(dx=0.1, dy=0.1, D=4.0):
    """
    Solves the 2D diffusion equation and outputs the results as plots.

    Parameters:
    - dx: float, grid spacing in the x-direction (default 0.1)
    - dy: float, grid spacing in the y-direction (default 0.1)
    - D: float, thermal diffusivity (default 4.0)
    """
    # Plate size, mm
    w = h = 10.0
    # Initial temperatures
    T_cold = 300
    T_hot = 700

    # Number of discrete mesh points in X and Y directions
    nx, ny = int(w / dx), int(h / dy)

    # Computing a stable time step
    dx2 = dx * dx
    dy2 = dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    print("dt = {}".format(dt))

    # Initialize the temperature grid
    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    # Set initial hot region in the center
    r = min(h, w) / 4.0
    cx, cy = w / 2.0, h / 2.0
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot

    # Number of timesteps
    nsteps = 101
    # Output 4 figures at these timesteps
    n_output = [0, 10, 50, 100]

    fig = plt.figure()
    im = None  # To store the image object for the color bar

    # Time loop
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

        # Create figure
        if n in n_output:
            position = 220 + n_output.index(n) + 1  # Define subplot position (221, 222, etc.)
            im = create_plot(u, T_cold, T_hot, dt, n, fig, position)

    # Plot output figures
    output_plots(fig, im)
