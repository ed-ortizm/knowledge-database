"""Setup script for sqlearning package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="sqlearning",
    version="0.1.0",
    author="Edgar Ortiz",
    author_email="ed.ortizm@gmail.com",
    packages=find_packages(
        where="src", include=["[a-z]*"], exclude=[]
    ),
    package_dir={"": "src"},
    description=(
        "Populate knowledge database with insights"
        "from latest trends in technology."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ed-ortizm/knowledge-database",
    license="Apache License 2.0",
    keywords="SQL, postgreSQL, json, technology, trends, insights",
)
