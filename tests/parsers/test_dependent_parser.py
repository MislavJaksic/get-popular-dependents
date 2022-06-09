# Auto-generated pytest file
import pytest
from bs4 import BeautifulSoup

from gpd.parsers.dependent_parser import DependentParser


@pytest.fixture(scope="module")
def middle_page_parser():
    with open("./tests/data/middle_network_dependents.html", "r") as file:
        html = file.read()
        soup = BeautifulSoup(html, "html.parser")
        first_dependent = soup.findAll("div", {"class": "Box-row"})[0]
        yield DependentParser(first_dependent)


# @pytest.fixture(scope="module")
# def first_page_parser():
#     with open("./tests/data/first_network_dependents.html", "r") as file:
#         html = file.read()
#         soup = BeautifulSoup(html, "html.parser")
#         first_dependent = soup.findAll("div", {"class": "Box-row"})[0]
#         yield DependentParser(first_dependent)


class TestGetAuthor:
    def test_get_author(self, middle_page_parser):
        data = middle_page_parser.get_author()
        assert data == "vutran1710"

    # def test_get_author_first(self, first_page_parser):
    #     data = first_page_parser.get_author()
    #     assert data == "vutran1710"


class TestGetName:
    def test_get_name(self, middle_page_parser):
        data = middle_page_parser.get_name()
        assert data == "Crypto-Code"


class TestGetStars:
    def test_get_stars(self, middle_page_parser):
        data = middle_page_parser.get_stars()
        assert data == 0


class TestGetForks:
    def test_get_forks(self, middle_page_parser):
        data = middle_page_parser.get_forks()
        assert data == 0


class TestGetUrl:
    def test_get_url(self, middle_page_parser):
        data = middle_page_parser.get_url()
        assert data == "https://github.com/vutran1710/Crypto-Code"


class TestGetUrlifyForGithub:
    def test_github_https_url(self, middle_page_parser):
        text = "https://github.com/vutran1710/Crypto-Code"
        data = middle_page_parser.urlify_for_github(text)
        assert data == text

    def test_github_http_url(self, middle_page_parser):
        text = "http://github.com/vutran1710/Crypto-Code"
        data = middle_page_parser.urlify_for_github(text)
        assert data == text

    def test_non_url(self, middle_page_parser):
        text = "/httparser/httparser"
        data = middle_page_parser.urlify_for_github(text)
        assert data == "https://github.com{}".format(text)


class TestGetHref:
    def test_get_href(self, middle_page_parser):
        data = middle_page_parser.get_href()
        assert data == "https://github.com/vutran1710/Crypto-Code"


class TestToDict:
    def test_to_dict(self, middle_page_parser):
        data = middle_page_parser.to_dict()
        assert data == {
            "author": "vutran1710",
            "forks": 0,
            "name": "Crypto-Code",
            "stars": 0,
            "url": "https://github.com/vutran1710/Crypto-Code",
        }
