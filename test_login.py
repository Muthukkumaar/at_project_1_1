import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver.get(url)

        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        # Add assertions to verify successful login
        sleep(2)  # Wait to ensure the page has time to load after login
        assert "dashboard" in self.driver.current_url, "Login failed or did not reach the dashboard"
