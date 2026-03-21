from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    service: Service = Service(ChromeDriverManager().install())
    options: webdriver.ChromeOptions = webdriver.ChromeOptions()
    browser: WebDriver = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
