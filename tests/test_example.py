from pages.home_page import HomePage


def test_google_title(driver):
    page = HomePage(driver)
    page.open()
    assert "Google" in page.get_title()


def test_search(driver):
    page = HomePage(driver)
    page.open()
    page.search("Selenium Python")
    assert "Selenium" in page.get_title()
