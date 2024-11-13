import setuptools
from setuptools import setup

if __name__ == "__main__":
    setup(name="bahiwaor_diffusion2d",
        version="0.0.1",
        author="Omkar Bahiwal",
        description="A package for solving the 2D diffusion equation",
        url="https://github.com/ombahiwal/diffusion2d-fork",
        package_dir={"": "bahiwaor-diffusion2d"},
        packages=setuptools.find_packages(where="bahiwaor-diffusion2d"),
        install_requires=["numpy", "matplotlib"],
        entry_points={
        'console_scripts': ['solve = bahiwaor_diffusion2d.diffusion2d:main']
        })