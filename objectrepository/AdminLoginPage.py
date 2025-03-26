from genral_utility.lib import SeleniumWrapper
from genral_utility.conftest import *

class Loginasadmin:
    admin_username=("xpath","//input[@name='username']")
    admin_password=("xpath","//input[@name='password']")
    loginbtn=("xpath","//button[@name='submit']")
    def __init__(self,driver):
        self.driver=driver
    def get_email(self):
        return self.admin_username

    def get_loginbtn(self):
        return self.loginbtn
    def get_password(self):
        return self.admin_password

    def admin_login(self, email, password):
        sw = SeleniumWrapper(self.driver)  # accessing the driver instance
#        sw.click_element(Login._lnk_login)
        sw.enter_text(Loginasadmin.admin_username, value=email)
        sw.enter_text(Loginasadmin.admin_password, value=password)
        sw.click_element(Loginasadmin.loginbtn)


