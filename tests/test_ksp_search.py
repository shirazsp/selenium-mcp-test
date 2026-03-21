import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def test_search_returns_results(driver):
    home = HomePage(driver)
    home.open()
    home.search("iphone")

    results = SearchResultsPage(driver)
    assert results.get_result_count() > 0, "Expected search results but got none"


def test_search_results_are_relevant(driver):
    home = HomePage(driver)
    home.open()
    home.search("iphone")

    results = SearchResultsPage(driver)
    assert results.results_contain("iphone"), "Expected results to contain 'iphone'"
