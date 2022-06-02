## GPD: Get Popular Dependents

Scope restricted to search for GitHub repository dependents. Can't find popular projects that use python's asyncio lobrary because it doesn't have a repository on GitHub.

```
# Note: Install Python 3
# Update pip and install virtualenv (dependency encapsulator) and black (linter; IDE needs to be restarted)

# Note: install Poetry for Linux
$: curl -sSL https://install.python-poetry.org | python3 -

# Note: install Poetry for Windows
$: (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

$: curl -sSL https://install.python-poetry.org | python3 - --uninstall
```

```
# Note: `.toml` project name and package have to match (gpd; gpd)
$: poetry install  # install all dependencies
```

More info about [poetry](https://github.com/MislavJaksic/Knowledge-Repository/tree/master/Technology/Software/BuildTool/poetry).

TAKE A LOOK AT READTHEDOCSS!

### dist

```
$: pip install dist/gpd-0.1.3-py3-none.any.whl

$: gpd
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### gpd

```
$: poetry run gpd -o Delgan -n loguru
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=gpd --cov-report=html tests
# Note: see coverage report in htmlcov/index.html
# Note: exclude directories from coverage report through .coveragerc
```

```
# TODO integration tests, pytest-integration
# TODO poetry run pytest --cov=eve_tools --cov-report=html -m "not integration_test" --integration-cover tests (it does not run integration test, but it also doesn't contribute to coverage)
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add [-D] Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.

### setup.cfg

Configure Python libraries.

### Linters

```
$: poetry run black .
```

### MyPy

```
$: poetry run mypy ./gpd ./tests
```

### cProfile

```
$: poetry run python ./gpd/profiler.py
```

### Build and publish

```
$: poetry build

# Note: get the token from your PiPy account
$: poetry config pypi-token.pypi PyPI-Api-Access-Token
```

```
$: poetry publish --build
```

```
https://pypi.org/project/gpd/
```
