from genral_utility.lib import SeleniumWrapper
from time import sleep

class Login:
    __name_email=("xpath","//input[@name='username']")
#    __lnk_login=("xpath","(//button[@class='btn btn-success btn-sm'])[2]")
    __txt_password=("xpath","//input[@name='password']")
    __btn_login=("xpath","//button[@name='submit']")
    def __init__(self,driver):
        self.driver=driver
    def get_email(self):
        return self.__name_email

    def get_loginbtn(self):
        return self.__btn_login
    def get_password(self):
        return self.__txt_password





    def login(self,email,password):
        sw = SeleniumWrapper(self.driver)  # accessing the driver instance
#        sw.click_element(Login._lnk_login)
        sw.enter_text(Login.__name_email, value=email)
        sw.enter_text(Login.__txt_password, value=password)
        sw.click_element(Login.__btn_login)
        sleep(1)



