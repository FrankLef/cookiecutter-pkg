# cookiecutter-pkg

<!-- badges: start -->
[![Lifecycle:
stable](https://img.shields.io/badge/lifecycle-stable-brightgreen)](https://lifecycle.r-lib.org/articles/stages)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-^3.10-blue)](https://www.python.org/downloads/release/python-3106/)
[![cookiecutter](https://img.shields.io/badge/cookiecutter-2.1.1-blueviolet)](https://cookiecutter.readthedocs.io/en/stable/)
[![Poetry](https://img.shields.io/badge/poetry-^1.7.1-purple)](https://pypi.org/project/poetry/)
[![Ruff](https://img.shields.io/badge/ruff-^0.2.2-maroon)](https://docs.astral.sh/ruff/)
[![Pre-commit](https://img.shields.io/badge/precommit-^3.5.0-orange)](https://pypi.org/project/pre-commit/)
<!-- badges: end -->

Cookiecutter for simple packages by Ephel. This cookiecutter tries to use
the most modern Python setup without the full complexity of [Hypermodern Python cookiecutter].

## Features

### Workflow

This cookiecutter proposes a workflow organized with [directory structure](#directory-structure).

The overall choices of packages is inspired from [Hypermodern Python cookiecutter].
The cookiecutter [data-science-template] by Khuyen Tran was also very useful.

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

Also, in case of bug, verify which environment and python version `poetry` is
using. Usually, different environments used by different python version
create problems with `poetry``.

To debug poetry you can use

    poetry debug info

and to see the list of environment available

    poetry env list

Sometimes, especially when reusing a folder that had been used as a project
before, the old environment is still used. To delete the old environment use

    poetry env remove <python>

Run `poetry shell` to open the poetry shell and avoid having to always add
`poetry run`in front of all commands

    poetry shell

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

Some directories, such as the `data/`, are included in `.gitignore` and therefore
ignored by the cookicutter which is coming from `git`. Run `make` to add these
extra directories. The most usual one is `data`.

    make ignored_dir

### Step 5 Install `pre-commit`

Once `.git` is setup, make sure to include the pre-commit script in `.git`
by running `pre-commit install` from the poetry shell. Also `pre-commit update`
ensures that the `ruff` is up-to-date. Sometimes warnings
appear about the 'rev' field being mutable, using `pre-commit update`
usually resolves this.

These steps are encoded in the Makefile and can be run as follows

    make precommit

It is also a good idea to run the hooks against all files when adding a new hook

    pre-commit run --all-files

wich is encoded in the MakeFile with the command

    make precommit_run

### Step 6 Verify the features

It is also useful to test the features of the new project before embarking
in the coding.

#### Code source linter and formatter

To run the linter from `ruff check .` use the command

    make lint

To run the code formatter from `ruff format .` use the command

    make format

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

Also you need to modify the project's `pyproject.toml` file to allow `poetry`
to use it in its environnment as follow

    [tool.poetry.dev-dependencies]
    igclib = {path = "../path/package", develop = true}

## Help notes

Some configurations needed to be changed when problems
were encountered. They are described as well as their solutions below.

You can also read the `pyproject.toml` provided by this cookiecutter to see
info on the required changes.

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
|[ruff]|Fast (very) Python linter and code formatter, written in Rust.|
|[pre-commit]|Manage pre-commit hooks|
|[pre-commit-hooks]|Some out-of-the-box hooks for `pre-commit`|
|[pytest]|Framework for testing|
|[mypy]|Static type checker|
|[typeguard]|Type checking for functions|

### Documentation

|Library|Description|
|:-----|:-----------------|
|[MkDocs]|Project documentation|
|[mkdocstrings]|Automatic documentation|
|[mkdocstrings-python]|Automatic documentation|

### Project Libraries

|Library|Description|
|:-----|:-----------------|
|[rich]|Writing rich text to the terminal and display advanced content|
|[typer]|Typer, build great CLIs|
|[dynaconf]|Settings management|
|[tomli]|A lil' TOML parser|
|[requests]|HTTP library for Python|
|[pandas]|Data analysis and manipulation tool|
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
[data-science-template]: https://github.com/khuyentran1401/data-science-template
[poetry]: https://pypi.org/project/poetry/
[ruff]: https://docs.astral.sh/ruff/
[pre-commit]: https://pypi.org/project/pre-commit/
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[pytest]: https://pypi.org/project/pytest/
[mypy]: http://www.mypy-lang.org
[typeguard]: https://typeguard.readthedocs.io/en/latest/
[MkDocs]: https://www.mkdocs.org
[mkdocstrings]: https://mkdocstrings.github.io
[mkdocstrings-python]: https://mkdocstrings.github.io/python/
[dynaconf]: https://www.dynaconf.com
[rich]: https://rich.readthedocs.io/en/stable/introduction.html
[typer]: https://typer.tiangolo.com
[tomli]: https://pypi.org/project/tomli/
[requests]: https://requests.readthedocs.io/en/latest/
[pandas]: https://pandas.pydata.org
[numpy]: https://numpy.org
[pyodbc]: https://pypi.org/project/pyodbc/
[SQLAlchemy]: https://www.sqlalchemy.org
