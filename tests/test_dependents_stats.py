# Auto-generated pytest file
import pytest

from gpd.dependents_stats import DependentsStats


@pytest.fixture(scope="module")
def stats(sample_dependents):
    yield DependentsStats(sample_dependents)

class TestGetCount:
    def test_get_count(self, stats):
        data = stats.get_count()
        assert data == len(stats.dependents)


class TestGetTopStars:
    def test_get_top_stars(self, stats):
        max = 3
        data = stats.get_top_stars(max)
        assert data.find("https://github.com/B/E") == 194

class TestGetTopForks:
    def test_get_top_forks(self, stats):
        max = 3
        data = stats.get_top_forks(max)
        assert data.find("https://github.com/B/E") == 194

class TestGroupDependentsByKey:
    def test_group_dependents_by_key(self, stats, sample_dependents):
        data = stats._group_dependents_by_key(sample_dependents)
        assert data == {'name': ['C', 'B', 'A'], 'stars': [3, 2, 1], 'forks': [6, 5, 4], 'author': ['F', 'E', 'D'], 'url': ['https://github.com/C/F', 'https://github.com/B/E', 'https://github.com/A/D']}

