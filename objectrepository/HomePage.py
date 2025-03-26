from genral_utility.lib import SeleniumWrapper
from time import sleep


class home_page:
    _logins_button=("xpath","//a[text()='Logins']")
    admin_loginbtn=("xpath"," //h6[.='Admin Login']/..//button[.='Click Here']")
    patient_loginbtn=("xpath"," //h6[.='Patient Login']/..//button[.='Click Here']")
    doctor_loginbutton=("xpath"," //h6[.='Doctors login']/..//button[.='Click Here']")
    def __init__(self,driver):
        self.driver=driver
    def get_logins_button(self):
        return self.logins_button
    def get_admin_loginbtn(self):
        return self.admin_loginbtn
    def get_patient_loginbtn(self):
        return self.patient_loginbtn
    def get_doctor_loginbtn(self):
        return self.doctor_loginbutton
    def click_logins_button(self):
        self.driver.find_element("xpath", "//a[text()='Logins']").click()
        sleep(5)
    def click_admin_loginbutton(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(home_page.admin_loginbtn)
    def click_doctor_loginbutton(self):
        sw = SeleniumWrapper(self.driver)
        sw.click_element(home_page.doctor_loginbutton)
    def click_patient_loginbutton(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(home_page.patient_loginbtn)






