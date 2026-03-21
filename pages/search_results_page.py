from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:
    PRODUCT_LINKS = (By.CSS_SELECTOR, "a[href*='/web/item/']")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "a[class*='productTitle']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_results(self):
        self.wait.until(EC.presence_of_element_located(self.PRODUCT_LINKS))

    def get_product_titles(self):
        self.wait_for_results()
        titles = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [t.text.strip() for t in titles if t.text.strip()]

    def get_result_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_LINKS)) // 2  # each item has image + title link

    def results_contain(self, keyword):
        titles = self.get_product_titles()
        return any(keyword.lower() in title.lower() for title in titles)
