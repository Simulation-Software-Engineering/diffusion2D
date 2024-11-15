"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from output import create_plot, output_plots

# plate size, mm
w = h = 10.
# intervals in x-, y- directions, mm
dx = dy = 0.1
# Thermal diffusivity of steel, mm^2/s
D = 4.

# Initial cold temperature of square domain
T_cold = 300

# Initial hot temperature of circular disc at the center
T_hot = 700

# Number of discrete mesh points in X and Y directions
nx, ny = int(w / dx), int(h / dy)

# Computing a stable time step
dx2, dy2 = dx * dx, dy * dy
dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

print("dt = {}".format(dt))

u0 = T_cold * np.ones((nx, ny))
u = u0.copy()

# Initial conditions - circle of radius r centred at (cx,cy) (mm)
r = min(h, w) / 4.0
cx = w / 2.0
cy = h / 2.0
r2 = r ** 2
for i in range(nx):
    for j in range(ny):
        p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
        if p2 < r2:
            u0[i, j] = T_hot


def do_timestep(u_nm1, u, D, dt, dx2, dy2):
    u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
            (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
            + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)
    u_nm1 = u.copy()
    return u_nm1, u

# Solver function
def solve(dx=0.1, dy=0.1, D=4.0):
    w = h = 10.0
    T_cold = 300
    T_hot = 700
    nx, ny = int(w / dx), int(h / dy)
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()
    r = min(h, w) / 4.0
    cx = w / 2.0
    cy = h / 2.0
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot

    nsteps = 101
    n_output = [0, 10, 50, 100]
    fig = plt.figure()
    fig_counter = 0
    im = None

    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)
        if n in n_output:
            fig_counter += 1
            im = create_plot(fig, u, T_cold, T_hot, dt, n, fig_counter)

    output_plots(fig, im)

# Running the solve function as a test
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 diffusion2d.py <dx> <dy> <D>")
    else:
        dx = float(sys.argv[2])
        dy = float(sys.argv[3])
        D = float(sys.argv[4])           
        print(f'dx={dx}, dy={dy}, D={D}')

        solve(dx, dy, D)