from setuptools import setup
import setuptools

setup(
    author="Johannes_Zipfel",
    url="https://github.com/johzip/diffusion2D/blob/main/diffusion2d.py",
    package_dir={"": "zipfeljs_diffusion2d"},
    packages=setuptools.find_packages(where="zipfeljs_diffusion2d")
)