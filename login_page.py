from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_locator = 'username'
        self.password_locator = 'password'
        self.submit_button_locator = '//button[@type="submit"]'

    def enter_username(self, username: str):
        try:
            webelement_of_username = self.driver.find_element(By.NAME, self.username_locator)
            webelement_of_username.send_keys(username)
        except Exception as e:
            print(f"Error entering username: {e}")

    def enter_password(self, password: str):
        try:
            webelement_of_password = self.driver.find_element(By.NAME, self.password_locator)
            webelement_of_password.send_keys(password)
        except Exception as e:
            print(f"Error entering password: {e}")

    def click_login(self):
        try:
            webelement_of_submit_button = self.driver.find_element(By.XPATH, self.submit_button_locator)
            webelement_of_submit_button.click()
        except Exception as e:
            print(f"Error clicking login button: {e}")
