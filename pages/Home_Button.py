from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeButton:

    def __init__(self, driver):
        self.driver = driver
        self.menubutton = (By.XPATH, "//i[@class='fa fa-bars']")
        self.homebutton = (By.XPATH, "//a[normalize-space()='Home']")

    def menu(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.menubutton)).click()

    def home(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.homebutton)).click()
