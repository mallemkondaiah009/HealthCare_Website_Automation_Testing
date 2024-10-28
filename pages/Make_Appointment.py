from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
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

    def make_appointment(self):
        self.driver.find_element(*self.make_appointment_button).click()

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def select_facility(self, facility_name):
        facility_dropdown_element = self.driver.find_element(*self.facility_dropdown)
        Select(facility_dropdown_element).select_by_visible_text(facility_name)

    def enable_hospital_readmission(self):
        self.driver.find_element(*self.hospital_readmission_checkbox).click()

    def select_medicare_program(self):
        self.driver.find_element(*self.medicare_radio).click()

    def enter_visit_date(self, visit_date):
        self.driver.find_element(*self.visit_date_field).send_keys(visit_date)

    def enter_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def book_appointment(self):
        self.driver.find_element(*self.book_appointment_button).click()
