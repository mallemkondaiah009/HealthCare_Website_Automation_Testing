import pytest
from pages.Make_Appointment import AppointmentPage


@pytest.mark.usefixtures("init_driver")
class TestAppointment:

    def test_book_appointment(self):
        self.driver.get("https://katalon-demo-cura.herokuapp.com/#history")
        # Initialize AppointmentPage object
        appointment_page = AppointmentPage(self.driver)

        # Perform actions
        appointment_page.make_appointment()
        appointment_page.login("John Doe", "ThisIsNotAPassword")
        appointment_page.select_facility("Tokyo CURA Healthcare Center")
        appointment_page.enable_hospital_readmission()
        appointment_page.select_medicare_program()
        appointment_page.enter_visit_date("25/05/2025")
        appointment_page.enter_comment("I am suffering from fever")
        appointment_page.book_appointment()
        appointment_page.go_home()

        # You could add verification steps here if needed
