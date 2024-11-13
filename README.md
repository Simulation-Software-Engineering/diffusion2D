# diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This an example python library, that solves diffusion equations in 2D.

The code solves the equations over a square domain, which is at a fixed temperature.
A higher temperature is applied to a circular area in the center.

The method used for solving is the Finite Difference Method.

Some parameters, like the thermal diffusivity, may be changed.

The code creates four plots at some timesteps of the simulation.

For the theoretical background refer to [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)

## Installing the package

### Using pip3 to install from PyPI

Use 
```shell
 $ pip3 install \
        --index-url https://test.pypi.org/simple/ \
        --extra-index-url https://pypi.org/simple/ \
        krampfkn_diffusion2d
```

to install the package from TestPyPI.


### Required dependencies

The requirements for using this code are:
 - `matplotlib>=3.9`
 - `numpy>=2.1`

All dependencies should be available in reasonably recent versions.
In some cases older versions might work, but have not been tested.

## Running this package

A minimal example to run this code is given below:

```python
from krampfkn_diffusion2d.diffusion2d import solve

solve(
    4., # D: Thermal diffusivity
    .1, # dx: Discrete Interval for x-direction
    .1  # dy: Discrete Interval for y-direction
)
```

## Citing

When citing this repository use this reference:

```bibtex
@misc{diffusion2d_2024,
    url = {https://github.com/Simulation-Software-Engineering/diffusion2D},
    author = {Krampf, Kilian \and Desai, Ishaan},
    title = {diffusion2D},
    subtitle = {Example python code for packaging},
    year = {2024},
}
```

