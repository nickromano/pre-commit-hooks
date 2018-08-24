from setuptools import find_packages
from setuptools import setup


setup(
    name="nr_pre_commit_hooks",
    description="Pre commit hooks.",
    url="https://github.com/nickromano/pre-commit-hooks",
    version="0.0.1",
    author="Nick Romano",
    author_email="nick.r.romano@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(exclude=("tests*", "testing*")),
    install_requires=["flake8", "mypy", "black", "django"],
    entry_points={"console_scripts": []},
)
