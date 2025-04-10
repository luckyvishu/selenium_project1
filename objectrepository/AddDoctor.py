from genral_utility.lib import SeleniumWrapper
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class Adddoctor():
    doctor_click=("xpath","//span[text()=' Doctors ']")
    add_doctor_click=("xpath","//span[contains(text(), 'Add Doctor')]")
    SpecializationDp=("name","Doctorspecialization")
    Doc_name=("xpath", "//input[@name='docname']")
    Docaddress=("xpath","//textarea[@name='clinicaddress']")
    Docfee=("xpath","//input[@name='docfees']")
    Doccontact=("xpath","//input[@name='doccontact']")
    Docemail=("xpath","//input[@name='docemail']")
    Docpassword=("xpath","//input[@name='npass']")
    Docconpass=("xpath","//input[@name='cfpass']")
    submitbtn=("xpath","//button[@name='submit']")
    def __init__(self,driver):
        self.driver=driver

    def add_Docotor(self,name,address,fee,contact,email,password,conformpassword):
        sw = SeleniumWrapper(self.driver)
        sw.click_element(Adddoctor.doctor_click)
        sw.click_element(Adddoctor.add_doctor_click)
#        sw.select_element_by_value(Adddoctor.SpecializationDp,value="Dermatologist")
        element = self.driver.find_element("name", "Doctorspecialization")
        s = Select(element)
        s.select_by_value("Dermatologist")

        sw.enter_text(Adddoctor.Doc_name,value=name)
        sw.enter_text(Adddoctor.Docaddress,value=address)
        sw.enter_text(Adddoctor.Docfee,value=fee)
        sw.enter_text(Adddoctor.Doccontact,value=contact)
        sw.enter_text(Adddoctor.Docemail,value=email)
        sw.enter_text(Adddoctor.Docpassword,value=password)
        sw.enter_text(Adddoctor.Docconpass,value=conformpassword)
        sleep(1)
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        actions = ActionChains(self.driver)
        actions.move_to_element(button).click().perform()


        sleep(2)
        self.driver.switch_to.alert.accept()

        sleep(2)






