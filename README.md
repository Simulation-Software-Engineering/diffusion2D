# diffusion2D

# Project description
A 2D diffusion equation solver with visualization output that used matplotlib and numpy to plot 3 graphs. The project can take arguements for values of dx, dy and D to compute and visualize the 2D diffusion and use matplotlib to plot the figures.

## Installing the package
You can use pip to directly install the package or build it from source using pip from the tar.gz/.whl package from [TestPyPi](link)

### Using pip3 to install from PyPI
To install the package, simply run:
```console
pip install -i https://test.pypi.org/simple/ ahmedsa-diffusion2d
```

### Required dependencies
The required dependencies are:
- Python (version >= 3)
- pip
- NumPy
- Matplotlib
If you plan to build from source, you also need to install the **build** pip package.

## Running this package
To run the package, you can use the following command:
```console
python3 diffusion2d.py
```
Or if you prefer to pass values of dx, dy and D (respectively), you can pass them as arguements as follows:
```console
python3 diffusion2d.py solve <dx> <dy> <D>
```

## Citing
- [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)
- [Simulation Service Engineering Exercise](https://github.com/Simulation-Software-Engineering/diffusion2D)

