from genral_utility.lib import SeleniumWrapper


class Loginpatient:
    username=("xpath","//input[@name='username']")
    password=("xpath","//input[@name='password']")
    forgor_password=("xpath","//a[contains(text(),'Forgot Password')]")
    login_btn=("xpath","//button[@name='submit']")
    create_link=("partial link text","Create")
    login_link = ("xpath", "//a[contains(text(), 'Log-in')]")
    def __init__(self,driver):
        self.driver=driver
    def Create_Link(self):

        self.driver.find_element("partial link text","Create").click()
    def Login_link(self):
        self.driver.find_element("xpath", "//a[contains(text(), 'Log-in')]").click()
    def Forgot_link(self):
        return self.driver.find_element(Loginpatient.forgor_password)
    def login_patient(self,username,password):
        sw=SeleniumWrapper(self.driver)
        sw.enter_text(Loginpatient.username,value=username)
        sw.enter_text(Loginpatient.password,value=password)
        sw.click_element(Loginpatient.login_btn)