from selenium.webdriver.common.by import By


class HomePage:
    URL = "https://www.google.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def search(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()

    def get_title(self):
        return self.driver.title
