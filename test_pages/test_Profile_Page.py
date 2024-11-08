# project/tests/test_navigation.py
import pytest
from pages.Profile_Page import ProfilePage

@pytest.mark.usefixtures("login")  # Use the login fixture from conftest.py
class TestNavigation:
    def test_navigate_to_profile(self):
        nav_page = ProfilePage(self.driver)

        # Use the methods in NavigationPage to open the menu and navigate to the profile
        nav_page.open_menu()
        nav_page.go_to_profile()


