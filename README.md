# diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

Direct installation is possible from PyPI by using the following command:

```sh
pip install -i https://test.pypi.org/simple/ puranivt-diffusion2d==0.0.1
```

### Required dependencies

The following dependencies will be automatically installed:

1. `numpy`: It supports large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
2. `matplotlib`: A plotting library commonly used in Python. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits.

## Running this package

The equation solver is implemented in the `solve` function of the package. To make the code run:

Simply open a python shell and run the following commands:

```python
from puranivt_diffusion2d.diffusion2d import solve

solve(dx = 0.1, dy = 0.1, D = 4)
```
Play around with the values of these parameters to observe changes in the output.

## Citing

```bibtex
@software{puranivt_diffusion2d,
  author       = {Vedant Puranik},
  title        = {{{puranivt_diffusion2d}: A project that implementes the diffusion equation solver over a series of timesteps based on configurable parameters: (dx, dy, D)}},
  year         = {2024},
  version      = {0.0.1},
  url          = {"https://github.com/VedantKP/diffusion2D"},
}
```