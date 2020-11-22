import io
import os

from setuptools import find_packages, setup


NAME = "deck_of_cards"
URL = ""
EMAIL = "atdifurio@gmail.com"
AUTHOR = "Andrew DiFurio"
PYTHON_REQUIRES = ">=3.7.0"
DESCRIPTION = "Deck of Cards"

setup(
    name=NAME,
    author=AUTHOR,
    email=EMAIL,
    url=URL,
    package_dir={"": "src"},
    packages=find_packages("src"),
    description=DESCRIPTION,
    python_requires=PYTHON_REQUIRES,
)
