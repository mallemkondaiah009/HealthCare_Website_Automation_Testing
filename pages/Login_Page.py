# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_toggle = (By.XPATH, "//a[@id='menu-toggle']")
        self.login_link = (By.XPATH, "//a[normalize-space()='Login']")
        self.username_field = (By.XPATH, "//input[@id='txt-username']")
        self.password_field = (By.XPATH, "//input[@id='txt-password']")
        self.login_button = (By.XPATH, "//button[@id='btn-login']")

    def open_menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.menu_toggle)).click()

    def click_login_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_link)).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def submit_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
