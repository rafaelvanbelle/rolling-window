import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rolling-window", # Replace with your own username
    version="0.0.1",
    author="Rafael Van Belle",
    author_email="rafael@gmail.com",
    description="Rolling Window based train/test split",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelvanbelle/rolling-window",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)