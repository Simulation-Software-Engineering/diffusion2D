# diffusion2D 

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package manually

The following steps install the package from source:

1. `git clone https://github.com/legendofa/diffusion2D`

2. `cd diffusion2D`

3. `pip install .`

### Using pip3 to install from PyPI

The package can be installed from the TestPyPI: 

`pip install --index-url https://test.pypi.org/simple/ kieslijn_diffusion2d --extra-index-url https://pypi.org/simple`

### Required dependencies

[Numpy](https://numpy.org) and [Matplotlib](https://matplotlib.org) are installed as dependencies when installing this packages, due to the `--extra-index-url https://pypi.org/simple` flag. Note that Matplotlib require some [backend dependencies](https://matplotlib.org/stable/install/dependencies.html#backends) in order to function properly.
No further dependencies are required.

## Running this package

The package offers the `solve` function which runs a diffusion simulation with the parameters:

- `dx` intervals in x-direction, unit $mm$
    - Describes how many spacial points are simulated in the x-direction of the circular disk
- `dy` intervals in y-direction, unit $mm$
    - Describes how many spacial points are simulated in the y-direction of the circular disk
- `D` thermal diffusivity in $\frac{mm^2}{s}$
    - Describes the material properties that the disk is made of
    - For example `4`, as the diffusivity of steel

## Citing

More information about the original project source and its math can be found at:
- https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
