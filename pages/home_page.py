from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL: str = "https://www.ksp.co.il"
    SEARCH_BOX: tuple = (By.ID, "searchTextBox")
    SEARCH_BUTTON: tuple = (By.CSS_SELECTOR, "div[class*='submitButton']")
    COOKIE_BUTTON: tuple = (By.XPATH, "//button[contains(text(), 'קראתי')]")
    POPUP: tuple = (By.CSS_SELECTOR, "div[class*='messageMenuBlock']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def open(self) -> None:
        self.driver.get(self.URL)
        self._dismiss_overlays()

    def _dismiss_overlays(self) -> None:
        try:
            cookie_btn: WebElement = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            cookie_btn.click()
        except Exception:
            pass

        try:
            popup: WebElement = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.POPUP)
            )
            self.driver.execute_script("arguments[0].style.display='none';", popup)
        except Exception:
            pass

    def search(self, query: str) -> None:
        search_box: WebElement = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        search_box.clear()
        search_box.send_keys(query)
        search_btn: WebElement = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        self.driver.execute_script("arguments[0].click();", search_btn)
