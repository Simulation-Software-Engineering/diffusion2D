from kieslijn_diffusion2d import diffusion2d

# intervals in x-, y- directions, mm
dx = dy = 1
# Thermal diffusivity of steel, mm^2/s
D = 4.

diffusion2d.solve(dx, dy, D)
