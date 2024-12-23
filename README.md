# cookiecutter-pkg

<!-- badges: start -->
[![Lifecycle:
stable](https://img.shields.io/badge/lifecycle-stable-brightgreen)](https://lifecycle.r-lib.org/articles/stages)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-^3.10-blue)](https://www.python.org/downloads/release/python-3106/)
[![Poetry](https://img.shields.io/badge/poetry-^1.8.2-purple)](https://pypi.org/project/poetry/)
[![Ruff](https://img.shields.io/badge/ruff-^0.3.1-maroon)](https://docs.astral.sh/ruff/)
[![Pre-commit](https://img.shields.io/badge/precommit-^3.6.2-orange)](https://pypi.org/project/pre-commit/)
[![MkDocs](https://img.shields.io/badge/mkdocs-^1.5.3-blueviolet)](https://www.mkdocs.org)
<!-- badges: end -->

Cookiecutter for simple packages using the most up-to-date setup possible.
Heavily inspired by [Hypermodern-cookiecutter], [cookiecutter-modern-datascience] and
[data-science-template] to whom we are very grateful.

The workflow is organized with this [directory structure](#directory-structure).

## Quickstart

`Makefile` is used repeatedly hereinafter to automate many of
the tasks. It is automatically configured by the cookiecutter to include, the
repo name, project name, etc.

### Step 1 Setup the project structure with `cookiecutter`

The rules for package names seem to be very strict in `poetry`. Please read the
following to avoid a lot of frustrating experiences.

> **Important note on the package name**: When using underscore in a package
name, `poetry` replaces underscore with dashes internally. Yet Python does not
recognize package name with a dash in script.  I have spent a lot ot time
trying to fix this. So my current standard is to use a **fullname** such as
`pkTodo` instead of `pk-todo` or `pk_todo`.

and, also, pay attention to the following

> **Important note on the package name, again!**: Only use lowercase names.
For some reason `poetry` dows not recognise `pkTodo` when updating! It only
works with `pkTodo`. Something is weird here but I can't find what it is or if
this is a normal constraint with `poetry`.

Change to the parent location where you want the project to be created.
For example if your project is called `pkTodo` in the `parent` folder,
then move to `parent` first

```console
cd ..\parent
```

verify that `cookiecutter` is properly installed by calling its version

```console
cookiecutter --version
```

then generate the project

```console
cookiecutter https://github.com/FrankLef/cookiecutter-pkg.git
```

and make the new folder the working directory.

```console
cd ..\parent\{{cookiecutter.__package_slug}}
```

### Step 2 Manage the dependencies with `poetry`

Don't forget to consult the [help poetry](#help-poetry) section in case of
problem of for more details.

Make sure the poetry version used is at least 1.7.

```console
poetry --version
```

Run `poetry shell` to open the poetry shell and avoid using `poetry run` with
all commands

```console
poetry shell
```

Run the `make` command `poetry_update`. To update the virutal environment.

```console
make poetry_update
```

### Step 3 Setup the new `.git`

#### Create repo in `github`

First create the new repo in github

* **Give the repo the exact same name as the package**.
* Don't create `README`, `.gitignore` and `LICENSE`. They will be created by
the cookiecutter.

#### Initialize the repo

Then initialize git using

```console
make git_init
```

### Step 4 Install `pre-commit`

See the [help pre-commit](#help-pre-commit-update) for details.

Setup and update `pre-commit`

```console
make precommit
```

It is also a good idea to run the hooks against all files to verify them.

```console
make precommit_run
```

### Step 5 Verify the features

#### Create the documentation with `mkdocs`

You can also verify that the documentation setup is working by building
the site.

```console
mkdocs serve
```

This will give you and output like this

```text
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.11 seconds
INFO    -  [09:26:11] Watching paths for changes: 'docs', 'mkdocs.yaml'
INFO    -  [09:26:11] Serving on http://127.0.0.1:8000/
INFO    -  [09:26:31] Browser connected: http://127.0.0.1:8000/
```

you can see the resulting documentation by ctrl-click on `http://127.0.0.1:8000/`

and when you are done, you can exit the result with

```console
ctrl^C
```

#### Code testing with `pytest`

Finally you can verify that `pytest` is working as expected. Use
this command wich runs the tests from the `tests` directory.

```console
pytest
```

### Step 6 (optional) Add the ignored directories

Some directories, such as the `\data`, are included in `.gitignore` and
therefore ignored by the cookicutter. You can run `make` to add these extra
directories.

```console
make ignored_dir
```

## Install and use the package

Assume all of the above went well and the packages contains features ready to
be used by projects or other python packages.

Then do the 2 steps below to use the package in some other project or package.

For illustration we assume we have a package called `pkTodo` located in

```text
C:/Users/Public/MyPy/Packages/pkTodo
```

### Step 1 Install the package

`poetry install` install the package in *editable mode*. That is it install
a link to the package on the computer rather than as an independent piece of
software. This is very useful to make the code available as soon as it is
modified when it is imported again.

You must be in the the package `pkTodo` located in
`C:/Users/Public/MyPy/Packages/pkTodo`

```console
cd ..\parent\{{cookiecutter.__package_slug}}
```

then you run the poetry install

```console
poetry install
```

### Step 2 Use the package in a project

To use the package in a project you need to do the following steps *when
you are in the project that needs to use the package*

#### Modify `pyproject.toml`

Change the '[tool.poetry]' section with

```text
[tool.poetry]
packages = [
{include = "pkTodo", from = "C:/Users/Public/MyPy/Packages/pkTodo"},
]
```

Change the '[tool.poetry.dependencies]' section with

```text
[tool.poetry.dependencies]
pkTodo = {path = "C:/Users/Public/MyPy/Packages/pkTodo", develop = true}
```

#### Update the poetry virtual environment

Just run the make command as above

```console
make poetry_update
```

Every thing should work fine now.

### Poetry shell

The package is only useable when you are in the virtual environment.
If you use the poetry shell with

```console
poetry shell
```

then you will loose the history in the `cmd` that is usually accessible in
the 'cmd'. To avoid that, don't start the shell and use

```console
poetry run python -m src --help
```

This is a known issue discussed in [github](https://github.com/python-poetry/poetry/issues/5050)
and [stackoverflow](https://stackoverflow.com/questions/69766163/on-windows-why-does-poetry-shell-remove-lose-shell-history-features).
These threads provide a hack to solve this. I don't use it.

### Help `reportMissingImports`

If this error can still happens

```text
Import {{cookiecutter.__package_slug}} could not be resolved Pylance(reportMissingImports)
```

#### Verify environment first

**This is important:** Make sure you are in the virtual environment, otherwise
pylane will say that the module not found. You can verify the environment in
VS Code on the lower right of the apps panel.

#### Environment problems

When the missing module error still come back, it is usually because of 2
different problems. **Both problems must be resolved** for the package to work.

These problems are

1. Wrong interpreter used by Visual Studio Code, see [Visual Studio Code environment](#visual-studio-code-environment)
2. Poetry virtual environment is desynchronized, see [Desynchronized virtual environment](#desynchronized-virtual-environment)

#### Visual Studio Code environment

This problem was resolved in [stack overflow](https://stackoverflow.com/questions/71229685/packages-installed-with-poetry-fail-to-import)

Verify the current environment you use

```console
poetry env info
```

and use `Ctrl+Shift P` to get `Python: Select Interpreter` to select your
environment identified by `poetry env info`.

This will tell VS Code to use the right environment to access the package
installed locally.

#### Desynchronized virtual environment

To manage the `poetry` environments, see the available commands at
[poetry](https://python-poetry.org/docs/managing-environments/). Also there is
some good tips at [Frank Mich](https://blog.frank-mich.com/poetry-explanations-and-tips/).

Sometimes the virtual environment is not synchronized with what is in
`pyproject.toml` and `poetry.lock`.

First you should have a look at your environment to see what is your active
environment

```console
poetry env info
```

and verify that your package is in the environment

```console
poetry show
```

then you reset it by deleting the `poetry.lock` and the virtual environment as
follows

```console
rm poetry.lock
poetry env remove test-O3eWbxRl-py3.7 (example environment)
```

and you rebuild them by **updating poetry**

```console
poetry update
```

After that, usually, it all works fine.  You should verify again that your
local package is in the virtual environment with

```console
poetry show
```

## Help notes

This section gives more details for reference and also to help solve problems
that were encountered and might happen again.

You can also read the `pyproject.toml` provided by this cookiecutter to see
information on the required changes.

### Help poetry

#### Help `poetry_update`

Run the `make` command `poetry_update` so that the following `poetry` command
will run

1. `poetry update`: The `poetry.lock` file will be created and the virtual
environment updated with the right packages and versions
2. `poetry show`: To verify if there are inconsistencies

#### Help poetry environment

Sometimes, especially when reusing a folder that had been used as a project
before, the old environment is still used. To see the environment curently
opened by `poetry` use this

```console
poetry env list
```

To delete the old environment use this command

```console
poetry env remove <python>
```

### Help pre-commit

#### Help pre-commit update

Once `.git` is setup, make sure to include the pre-commit script in `.git`
by running `pre-commit install` from the poetry shell. Also `pre-commit update`
ensures that the `ruff` is up-to-date. Sometimes warnings
appear about the 'rev' field being mutable, using `pre-commit update`
usually resolves this.

#### Help pre-commit run

No need to run the linter and code formatter separately. Better yet,
you can run all the pre-commit hooks using this useful command

```console
pre-commit run --all-files
```

wich is encoded in the MakeFile with the command

```console
make precommit_run
```

### `pyarrow`

Use `pyarrow.feather` instead of `feather-format`, `feather.format` exists only
for backward compatibility. `pyarrow` should be installed with
`pip3 install pyarrow` in the local python. Don't install `pyarrow` with
`poetry add pyarrow` or you will get a whole lot of cryptic errors.

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

```text
{{<package_slug>}}
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
├── pypath.bat                <- A batch file to set the PYTHONPATH. Optional.
├── data                      <- Data directories used throughout the project.
│   ├── d0_temp               <- Temporary folder. These files can be deleted.
|   └── ...
├── docs                      <- GitHub pages website.
│   ├── explanation.md        <- Understanding-oriented documentation.
│   ├── how-to-guides.md      <- Problem-oriented documentation.
│   ├── index.md              <- The index page for the whole documentation.
│   ├── reference.md          <- Information-oriented documentation.
│   ├── tutorials.md          <- Learning-oriented documentation.
|   └── ...
|
├── src                       <- Store the source code.
│   └── {{<package_slug>}}    <- Package code folder.
│       ├── __init__.py       <- The module's initialize file.
│       ├── __main__.py       <- Main CLI entry point.
|       └── ...
└── tests                     <- All test and fixtures files used in testing.
    ├── __init__.py
    ├── fixtures              <- Where to put example inputs and outputs.
    │   ├── input.json        <- Test input data.
    │   └── output.json       <- Test output data.
    ├── test_samples.py       <- Test example to verify `pytest`.
    └── ...
```

[cookiecutter]: https://github.com/audreyr/cookiecutter
[Hypermodern-cookiecutter]: https://cookiecutter-hypermodern-python.readthedocs.io/en
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
