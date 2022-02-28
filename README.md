# Overview
This repository contains a very fundamental solution / example for Python's headache (pain in the ...) relative imports and packaging system. 

# Steps
- Create a `virtual environment` for preventing the dependency confliction of the other projects and the easy management for dependencies of the project that you working on:
```
>>> python3 -m venv env
```
We have created the `virtual environment` for our project. Now, we need to activate it:
```
>>> source env/bin/activate
```

- Creating the setup file:
```python
from setuptools import setup, find_packages

setup(
  name = "python-imports",
  version = "0.0.1",
  packages = find_packages()
)
```
This `find_packages` function will lookup to the root and find all packages. Then, we can use these packages (which we have create) in our project like an external package which have we get from PYPI.

**Q**: OK, but how can I create my own package?


**A**: In simple terms, if you create the `__init__.py` file in one of folders, Python will behave these folders as packages, even if the `__init__.py` file is empty!

- Now, we will install our package locally in editable mode with `pip`:
```
>>> pip install -e .
```

- Final folder structure:
```
├── main.py
├── package1/
│   ├── hello.py
│   └── __init__.py
├── package2/
│   ├── hello.py
│   └── __init__.py
├── env/
└── setup.py
```

- So, we are good to go! We can import our packages like this (in our example - check the `package1` and `package2` folders):
```python
# package2/hello.py

from package1.hello import hello_with_name


def hello_from_package2():
  print("Hello from package-2!")


def hello_with_name_package1():
  hello_with_name(name = "Python")
```