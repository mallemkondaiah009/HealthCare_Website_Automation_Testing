import pytest
from pages.Login_Page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:

    def test_login(self):
        # Initialize the driver and open the application URL
        self.driver.get("https://katalon-demo-cura.herokuapp.com/#history")

        # Initialize the LoginPage object
        login_page = LoginPage(self.driver)

        # Open the menu and click the login link
        login_page.open_menu()
        login_page.click_login_link()

        # Enter username and password
        login_page.enter_username("John Doe")
        login_page.enter_password("ThisIsNotAPassword")

        # Submit the login form
        login_page.submit_login()
