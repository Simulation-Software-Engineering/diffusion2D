from setuptools import setup
import versioneer

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        long_description=long_description,
        long_description_content_type="text/markdown",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )