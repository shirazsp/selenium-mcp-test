from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://www.ksp.co.il"
    SEARCH_BOX = (By.ID, "searchTextBox")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div[class*='submitButton']")
    COOKIE_BUTTON = (By.XPATH, "//button[contains(text(), 'קראתי')]")
    POPUP = (By.CSS_SELECTOR, "div[class*='messageMenuBlock']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self._dismiss_overlays()

    def _dismiss_overlays(self):
        try:
            cookie_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            cookie_btn.click()
        except Exception:
            pass

        try:
            popup = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.POPUP)
            )
            self.driver.execute_script("arguments[0].style.display='none';", popup)
        except Exception:
            pass

    def search(self, query):
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(query)
        search_btn = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        self.driver.execute_script("arguments[0].click();", search_btn)
