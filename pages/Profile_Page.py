# project/pages/navigation_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10-second explicit wait for elements

    def open_menu(self):
        menu_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='menu-toggle']"))
        )
        menu_button.click()

    def go_to_profile(self):
        profile_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Profile']"))
        )
        profile_link.click()
