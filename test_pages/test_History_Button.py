import pytest
from pages.History_Button import HistoryButton
from test_pages.test_Make_Appointment import TestAppointment

@pytest.mark.usefixtures("init_driver")
class TestHistoryButton:

    def test_history(self):
        # First, make an appointment by creating an instance of TestAppointment
        test_appointment = TestAppointment()
        test_appointment.driver = self.driver  # Pass the driver to the TestAppointment instance
        test_appointment.test_book_appointment()

        # Navigate to the history page
        self.driver.get("https://katalon-demo-cura.herokuapp.com/#history")

        # Initialize HistoryButton object
        history_button = HistoryButton(self.driver)
        history_button.menu()
        history_button.open_history()
        history_button.go_to_homepage()
