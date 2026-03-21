from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:
    PRODUCT_LINKS: tuple = (By.CSS_SELECTOR, "a[href*='/web/item/']")
    PRODUCT_TITLES: tuple = (By.CSS_SELECTOR, "a[class*='productTitle']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def wait_for_results(self) -> None:
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_LINKS))

    def get_product_titles(self) -> list[str]:
        self.wait_for_results()
        titles: list[WebElement] = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [t.text.strip() for t in titles if t.text.strip()]

    def get_result_count(self) -> int:
        return len(self.driver.find_elements(*self.PRODUCT_LINKS)) // 2

    def results_contain(self, keyword: str) -> bool:
        titles: list[str] = self.get_product_titles()
        return any(keyword.lower() in title.lower() for title in titles)
