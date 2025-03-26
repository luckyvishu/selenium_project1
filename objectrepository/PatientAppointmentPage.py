from genral_utility.lib import SeleniumWrapper
from time import sleep
from selenium.webdriver.support.select import Select
from genral_utility.scrolllingfile import *
class Bookappointment:
    book_btn=("xpath","//span[text()=' Book Appointment ']")
    SpecializationDp = ("name", "Doctorspecialization")
    doctor=("name","doctor")
    appointmentdate=("xpath","//input[@name='appdate']")
    appointmenttime=("xpath","//input[@name='apptime']")
    submit_btn=("xpath","//button[@name='submit']")


    def __init__(self,driver):
        self.driver=driver


    def Book_appointment(self,appointment_date):
        sw = SeleniumWrapper(self.driver)
        sw.click_element(Bookappointment.book_btn)
        sleep(2)
        element = self.driver.find_element("name", "Doctorspecialization")
        s = Select(element)
        s.select_by_value("Dermatologist")
        element1=self.driver.find_element("name","doctor")
        s1=Select(element1)
        sleep(2)
        s1.select_by_visible_text("vishwanath hm")

        sc=get_date(self.driver)

        sw.enter_text(Bookappointment.appointmentdate,value=sc.get_random_date(appointment_date))
        sw.enter_text(Bookappointment.appointmenttime,value=sc.get_random_time())
        self.driver.execute_script(f"window.scrollBy(0, 1700)")
        sw.click_element(Bookappointment.submit_btn)



