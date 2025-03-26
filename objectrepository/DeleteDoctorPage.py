

from genral_utility.lib import SeleniumWrapper


class Deletedocotrpage:
    get_delete_message=("xpath","//p[contains(text(),'data deleted !!')]")
    doctor_click=("xpath","//span[text()=' Doctors ']")
    manage_doctor_click=("xpath","//span[text()=' Manage Doctors ']")
    click_on_Xmark=("xpath","//i[@class='fa fa-times fa fa-white']")
    def __init__(self,driver):
        self.driver=driver
    def Deletedoctor(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(Deletedocotrpage.doctor_click)
        sw.click_element(Deletedocotrpage.manage_doctor_click)
    def getDeletedmessage(self):
        return self.driver.find_element("xpath","//p[contains(text(),'data deleted !!')]").text




