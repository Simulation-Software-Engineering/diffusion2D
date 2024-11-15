# diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
Diffusion2D solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.
If you are interested in the theoretical background of the code, please have a look in [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Installing the package


### Using pip3 to install from PyPI
```
pip install -i https://test.pypi.org/simple/ zipfeljs-diffusion2d==0.0.1
```
### Required dependencies
Check if your system has Python version >= 3.6 and update it if it is older than 3.6.

```
python --version
```
install pip, matplotlib and numpy

## Running this package
Run the code using python and running the solve function in diffusion2d.py
it has three parameters with these standard values:
```
dx = dy = 0.1
D = 4.
```
## Citing
