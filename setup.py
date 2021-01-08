import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chq",
    version="0.0.3",
    author="TangYi",
    author_email="adamtang0830@gmail.com",
    description="Hacktool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tangyi19/chq",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
