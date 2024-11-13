# diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI
pip install -i https://test.pypi.org/simple/ sashanje-diffusion2d --extra-index-url https://pypi.org/simple

### Required dependencies
matplotlib
numpy

## Running this package

```python
from sashanje_diffusion2d import diffusion2d

diffusion2d.solve(
    dx = 0.1, # intervals in x- direction, mm
    dy = 0.1, # intervals in y- direction, mm
    D = 4 # Thermal diffusivity of steel, mm^2/s
    )
```

## Citing
Forked from https://github.com/Simulation-Software-Engineering/diffusion2D
[pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md)
