# pytest only exposes fixtures in a file called conftest.py!

import pytest

from gpd.models.dependent import Dependent


@pytest.fixture(scope="package")
def sample_dependents():
    dep1 = Dependent(
        **{
            "name": "A",
            "stars": 1,
            "forks": 4,
            "author": "D",
            "url": "https://github.com/A/D",
        }
    )
    dep2 = Dependent(
        **{
            "name": "B",
            "stars": 2,
            "forks": 5,
            "author": "E",
            "url": "https://github.com/B/E",
        }
    )
    dep3 = Dependent(
        **{
            "name": "C",
            "stars": 3,
            "forks": 6,
            "author": "F",
            "url": "https://github.com/C/F",
        }
    )
    yield [dep1, dep2, dep3]


@pytest.fixture(scope="session")
def session_level():
    yield 1
