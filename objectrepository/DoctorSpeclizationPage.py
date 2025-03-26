from genral_utility.lib import SeleniumWrapper



class DocotrSpecializationpage:
    doctorSpecilization=("xpath","//span[text()=' Doctor Specialization ']")
    doctor_enterspecialization=("xpath","//input[@name='doctorspecilization']")
    submit_btn=("xpath","//button[@name='submit']")
    def __init__(self,driver):
        self.driver=driver
    def CreateSpecialization(self,doctorspecialization):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(DocotrSpecializationpage.doctorSpecilization)
        sw.enter_text(DocotrSpecializationpage.doctor_enterspecialization,value=doctorspecialization)
        sw.click_element(DocotrSpecializationpage.submit_btn)

