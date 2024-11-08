from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HistoryButton:
    def __init__(self, driver):
        self.driver = driver
        self.menu_toggle = (By.XPATH, "//i[@class='fa fa-bars']")
        self.history_link = (By.XPATH, "//a[normalize-space()='History']")
        self.homepage_link = (By.XPATH, "//a[@class='btn btn-default']")


    def menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.menu_toggle)).click()

    def open_history(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.history_link)).click()

    def go_to_homepage(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.homepage_link)).click()
