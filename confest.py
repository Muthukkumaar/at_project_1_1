import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
