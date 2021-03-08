import setuptools

setuptools.setup(
    name="sudokusolver",
    version="0.1.0",
    description="Solves sudoku puzzles",
    author="Kevin Coffey",
    author_email="kevdougful@gmail.com",
    py_modules="sudokusolver",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "attrs",
        "numpy",
    ],
    extras_require={
        "dev": ["pytest"]
    }
)
