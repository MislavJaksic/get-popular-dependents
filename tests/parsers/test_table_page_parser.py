# Auto-generated pytest file
import pytest

from gpd.models.dependent import Dependent
from gpd.parsers.table_page_parser import TablePageParser


@pytest.fixture(scope="module")
def middle_page_parser():
    with open("./tests/data/middle_network_dependents.html", "r") as file:
        html = file.read()
        yield TablePageParser(html)


class TestGetDependentsEstimate:
    def test_get_dependents_estimate(self, middle_page_parser):
        data = middle_page_parser.get_dependents_estimate()
        assert data == 16737

        
class TestGetDependents:
    def test_get_dependents(self, middle_page_parser):
        data = middle_page_parser.get_dependents()[4]
        dict = {"name": 'anothermirror', "stars": 0, "forks": 0, "author": 'Aadhar4u',
                "url": 'https://github.com/Aadhar4u/anothermirror'}
        assert data == Dependent(**dict)


class TestGetRows:
    def test_get_rows(self, middle_page_parser):
        data = str(middle_page_parser.get_rows()[4].contents[1])
        assert data == '<img alt="@Aadhar4u" class="avatar mr-2 avatar-user" height="20" src="Network%20Dependents%20%C2%B7%20Delgan_loguru%20%C2%B7%20GitHub_files/88808890.jpg" width="20"/>'


class TestGetNextPageUrl:
    def test_get_next_page_url(self, middle_page_parser):
        data = middle_page_parser.get_next_page_url()
        assert data == 'https://github.com/Delgan/loguru/network/dependents?dependents_after=MjE4MDQ2Mzc1NTc'

