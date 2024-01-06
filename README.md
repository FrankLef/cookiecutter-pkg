# cookiecutter-pkg

<!-- badges: start -->
[![Lifecycle:
stable](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://lifecycle.r-lib.org/articles/stages)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10.6-blue.svg)](https://www.python.org/downloads/release/python-3106/)
[![Poetry](https://img.shields.io/badge/poetry-1.1.15-purple)](https://pypi.org/project/poetry/)
![Black](https://img.shields.io/badge/black-22.8.0-orange)
![Pre-commit](https://img.shields.io/badge/precommit-2.20.0-blue)
<!-- badges: end -->

Cookiecutter for simple packages by Ephel. This cookiecutter tries to use
the most modern Python setup without the full complexity of [Hypermodern Python cookiecutter].

## Features

### Workflow

This cookiecutter proposes a workflow organized with [directory structure](#directory-structure).

The overall choices of packages is inspired from [Hypermodern Python cookiecutter].

## Quickstart

The file `Makefile` will be used repeatedly hereinafter to automate many of
the tasks. It automatically configured by the cookiecutter to include, the
repo name, project name, etc.

### Step 1 Setup the project structure with `cookiecutter`

Change to the parent location where you want the package to be created.
For example if your package is called `pkg-proj` in the `parent` folder,
then move to `parent` first

    cd ../parent

verify that `cookiecutter` is properly installed by calling its version

    cookiecutter --version

then generate the project

    cookiecutter https://github.com/FrankLef/cookiecutter-pkg.git

and **make the new folder the working directory**.

### Step 2 Manage the dependencies with `poetry`

#### Installation

**Very important:** Make sure the poetry version used is at least 1.7. Verify
with

    poetry --version.

Also, in case of bug verify which environment and python version `poetry` is
using. Usually, different environments used by different python version
create problems with `poetry``.

To debug poetry you can use

    poetry debug info

and to see the list of environment available

    poetry env list

Run `poetry shell` to open the poetry shell and avoid having to always add
`poetry run`in front of all commands

    poetry shell

Sometimes, especially when reusing a folder that had been used as a project
before, the old environment is still used. To delete the old environment use

    poetry env remove <python>

#### Usage

Run the `make` command `poetry_update` so that the following `poetry` command
will run

1. `poetry update`: The `poetry.lock` file will be created and the virtual
environment updated with the right packages and versions
2. `poetry show`: To verify if there are inconsistencies

These steps are encoded in the Makefile and can be run as follows

    make poetry_update

### Step 3 Setup the new `.git`

#### Create repo in `github`

First create the new repo in github

* **Give the repo the exact same name as the package**. That is keep the
underscore in the name when there one. i.e. flproj_todo is also flproj_todo
in github.
* Don't create `README`, `.gitignore` and `LICENSE` with the new repo they
will be overriden anyway.

#### Initialize the repo

Then initialize git using

    make git_init

### Step 4 Add the ignored directories (optional for packages)

Some directories, such as the `data/`, are included in `.gitignore` and therefoer
ignored by the cookicutter which is coming from `git`. Run `make` to add these
extra directories. The most usual one is `data`.

    make ignored_dir

### Step 5 Install `pre-commit`

Once `.git` is setup, make sure to include the pre-commit script in `.git`
by running `pre-commit install` from the poetry shell. Also `pre-commit update`
ensures that the `black`, `flake8` etc. are up-to-date. Sometimes warnings
appear about the 'rev' field being mutable, using this `pre-commit update`
usually resolves this.

These steps are encoded in the Makefile and can be run as follows

    make pre_commit

It is also a good idea to run the hooks against all files when adding a new hook

    pre-commit run --all-files

### Step 6 Verify the features

It is also useful to test the features of the new project before embarking
in the coding.

#### Code source format and check

To run `isort` and `flake8` and verify all is in order run this make command

    make lint

#### Create the documentation with `mkdocs`

You can also verify that the documentation setup is working by building
the site.

Note: For some reason I am unable to run mkdocs from `poetry` with

    poetry run mkdocs serve

As a result, the following command which must be run
**outside the `poetry shell`**. That is it **must be run from the terminal**.

    mkdocs serve

Then you update the documentation with

    mkdocs build

There is more information at [real python] on using `mkdocs`.

**Important:**

#### Code testing with `pytest`

Finally you can verify that `pytest` is working as expected by using
this command wich runs the tests from the `tests` directory.

    pytest

## Install package and use the local library

To install the package, run the following in the **windows environment**, not
the virtual environment created by `poetry`. Otherwise the project calling this
library will not be able to import it.

To validate the package is in the windows environment run

    pip list

Also you need to modify the project's `pyproject.toml` file to allow `poerty`
touse it in its environnment as follow

    [tool.poetry.dev-dependencies]
    igclib = {path = "../path/package", develop = true}

## Setup notes

Some configurations needed to be changed when problems
were encountered. They are described as well as their solutions below.

You can also read the `pyproject.toml` provided by this cookiecutter to see
info on the required changes.

### `flake8`

`flake8` reports error **E501** for lines exceeding the 79 length limit
recommended by PIP-8. Even when `black` is ok with it and even when all lines
are properly formatted and abide by the rule.

Several hours were spent trying to fix it. The solution used here is
as follows:

* Modify `pyproject.toml` to include a section **tools.flake8** to tell
`flake8` to ignore E501 with `ignore=E501`.
* Add the plugin `flake8-pyproject` to the **tool.poetry.dependencies** section
of `pyproject.toml` because `flake8` does not use the `pyproject.toml` except
when the `flake8-pyproject` is installed.
* Modify `.pre-commit-config.yaml` to add `args: [--ignore=E501]` to the
flake8 hook.

### `pyarrow`

Use `pyarrow.feather` instead of `feather-format`, `feather.format` exists only
for backward compatibility. `pyarrow` should be installed with
`pip3 install pyarrow` in the local python. Don't install `pyarrow` with
`poetry add pyarrow` or you will get a whole lotof cryptic errors.

## Libraries Used

The primary libraries used are described in sections as follows:

* Template and environment
* Code quality
* Documentation
* Project libraries

### Template and Environment

|Library|Description|
|:-----|:-----------------|
|[cookiecutter]|Project templates|
|[poetry]|Project dependency|

### Code quality

|Library|Description|
|:-----|:-----------------|
|[flake8]|Style guide enforcement|
|[pep8-naming]|Check PEP-8 naming conventions, plugin for `flake8`|
|[black]|Code formatter|
|[pre-commit]|Manage pre-commit hooks|
|[pre-commit-hooks]|Some out-of-the-box hooks for `pre-commit`|
|[pytest]|Framework for testing|
|[mypy]|Static type checker|
|[typeguard]|Type checking for functions|
|[isort]|Sort imports and separate them into sections and types|

### Documentation

|Library|Description|
|:-----|:-----------------|
|[MkDocs]|Project documentation|
|[mkdocstrings]|Automatic documentation|
|[mkdocstrings-python]|Automatic documentation|

### Project Libraries

|Library|Description|
|:-----|:-----------------|
|[dynaconf]|Settings management|
|[rich]|Writing rich text to the terminal and display advanced content|
|[tomli]|A lil' TOML parser|
|[requests]|HTTP library for Python|
|[prefect]|Manage the dataflow|
|[pandas]|Data analysis and manipulaiton tool|
|[numpy]|Scientific computing|
|[pyodbc]|Access ODBC database|
|[SQLAlchemy]|SQL toolkit and object relational mapper|

## Directory structure

This is how the new project will be organized.

    ├── .gitignore                <- GitHub's Python `.gitignore` customized for this project.
    ├── config.py                 <- Script used `dynaconf` to manage settings.
    ├── pre-commit-config.yaml    <- Settings for `pre-commit`.
    ├── LICENSE                   <- The project's license.
    ├── Makefile                  <- Scripts to automate tasks.
    ├── mkdocs.yaml               <- Settings for `mkdocs`.
    ├── pyproject.toml            <- Configuration file used by `poetry`.
    ├── settings.toml             <- Project's settings used by `dynaconf`.
    ├── .secrets.toml             <- Secret settings used by `dynaconf`.
    ├── README.md                 <- The top-level README for developers using this project.
    ├── docs                      <- GitHub pages website.
    │   ├── explanation.md        <- Understanding-oriented documentation.
    │   ├── how-to-guides.md      <- Problem-oriented documentation.
    │   ├── index.md              <- The index page for the whole documentation.
    │   ├── reference.md          <- Information-oriented documentation.
    │   ├── tutorials.md          <- Learning-oriented documentation.
    |   └── ...
    |
    ├── src                       <- Store the source code.
    │   └── {{<package>}}         <- Package code folder.
    │       ├── __init__.py
    │       ├── {{<package>}}.py  <- Main code file.
    |       └── ...
    └── tests                     <- All test and fixtures files used in testing.
        ├── __init__.py
        ├── fixtures              <- Where to put example inputs and outputs.
        │   ├── input.json        <- Test input data.
        │   └── output.json       <- Test output data.
        ├── test_samples.py       <- Test example to verify `pytest`.
        └── ...

[cookiecutter]: https://github.com/audreyr/cookiecutter
[Hypermodern Python cookiecutter]: https://cookiecutter-hypermodern-python.readthedocs.io/en/2020.6.15/index.html
[cookiecutter-modern-datascience]: https://github.com/crmne/cookiecutter-modern-datascience
[data-science-template]: https://github.com/khuyentran1401/data-science-template
[real python]: https://realpython.com/python-project-documentation-with-mkdocs/
[poetry]: https://pypi.org/project/poetry/
[flake8]: https://pypi.org/project/flake8/
[pep8-naming]: https://pythonfix.com/pkg/p/pep8-naming/
[black]: https://pypi.org/project/black/
[pre-commit]: https://pypi.org/project/pre-commit/
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[pytest]: https://pypi.org/project/pytest/
[mypy]: http://www.mypy-lang.org
[typeguard]: https://typeguard.readthedocs.io/en/latest/
[isort]: https://github.com/PyCQA/isort
[MkDocs]: https://www.mkdocs.org
[mkdocstrings]: https://mkdocstrings.github.io
[mkdocstrings-python]: https://mkdocstrings.github.io/python/
[dynaconf]: https://www.dynaconf.com
[rich]: https://rich.readthedocs.io/en/stable/introduction.html
[tomli]: https://pypi.org/project/tomli/
[requests]: https://requests.readthedocs.io/en/latest/
[prefect]: https://docs.prefect.io
[pandas]: https://pandas.pydata.org
[numpy]: https://numpy.org
[pyodbc]: https://pypi.org/project/pyodbc/
[SQLAlchemy]: https://www.sqlalchemy.org
