#!/usr/bin/env python
import setuptools


if __name__ == "__main__":
    setuptools.setup(
        author="Davi Raubach",
        author_email="davi@daviraubach.com",
        install_requires=("abjad",),
        name="organi",
        packages=("organi",),
        url="https://github.com/DaviRaubach/organi",
        version="0.1",
        zip_safe=False,
    )
