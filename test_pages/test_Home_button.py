import pytest
from pages.Home_Button import HomeButton  # Adjust this import path as necessary

@pytest.mark.usefixtures("init_driver")
class TestHomeButton:

    def test_navigate_to_home(self):
        # Initialize the driver and open the application URL
        self.driver.get("https://katalon-demo-cura.herokuapp.com/#history")

        # Initialize HomeButton object
        home_button = HomeButton(self.driver)

        # Open the menu
        home_button.menu()

        # Click the home button
        home_button.home()


