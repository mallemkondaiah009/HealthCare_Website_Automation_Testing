from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10-second wait for elements to be interactable

        # Define locators
        self.make_appointment_button = (By.XPATH, "//a[@id='btn-make-appointment']")
        self.username_field = (By.XPATH, "//input[@id='txt-username']")
        self.password_field = (By.XPATH, "//input[@id='txt-password']")
        self.login_button = (By.XPATH, "//button[@id='btn-login']")
        self.facility_dropdown = (By.XPATH, "//select[@id='combo_facility']")
        self.hospital_readmission_checkbox = (By.XPATH, "//input[@id='chk_hospotal_readmission']")
        self.medicare_radio = (By.XPATH, "//input[@id='radio_program_medicare']")
        self.visit_date_field = (By.XPATH, "//input[@id='txt_visit_date']")
        self.comment_field = (By.XPATH, "//textarea[@id='txt_comment']")
        self.book_appointment_button = (By.XPATH, "//button[@id='btn-book-appointment']")
        self.go_to_home=(By.XPATH,"//a[@class='btn btn-default']")

    def make_appointment(self):
        self.wait.until(EC.element_to_be_clickable(self.make_appointment_button)).click()

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def select_facility(self, facility_name):
        facility_dropdown_element = self.wait.until(EC.visibility_of_element_located(self.facility_dropdown))
        Select(facility_dropdown_element).select_by_visible_text(facility_name)

    def enable_hospital_readmission(self):
        self.wait.until(EC.element_to_be_clickable(self.hospital_readmission_checkbox)).click()

    def select_medicare_program(self):
        self.wait.until(EC.element_to_be_clickable(self.medicare_radio)).click()

    def enter_visit_date(self, visit_date):
        self.wait.until(EC.visibility_of_element_located(self.visit_date_field)).send_keys(visit_date)

    def enter_comment(self, comment):
        self.wait.until(EC.visibility_of_element_located(self.comment_field)).send_keys(comment)

    def book_appointment(self):
        self.wait.until(EC.element_to_be_clickable(self.book_appointment_button)).click()

    def go_home(self):
        self.wait.until(EC.element_to_be_clickable(self.go_to_home)).click()
