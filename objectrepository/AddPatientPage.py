from genral_utility.lib import SeleniumWrapper


class Addpatient:
    click_patient=("xpath","//span[text()=' Patients ']")
    click_appointment=("xpath","//span[text()=' Appointment History ']")
    click_addpatient=("xpath","//span[text()=' Add Patient']")
    pat_name=("xpath","//input[@name='patname']")
    pat_contact=("xpath","//input[@name='patcontact']")
    pat_email=("xpath","//input[@name='patemail']")
    pat_gender_male=("xpath","//label[contains(text(),'Male')]")
    pat_gender_female=("xpath","//label[contains(text(),'Female')]")
    pat_address=("xpath","//textarea[@name='pataddress']")
    pat_age=("xpath","//input[@name='patage']")
    pat_med_his=("xpath","//textarea[@name='medhis']")
    add_button=("xpath","//button[@type='submit']")
    def __init__(self,driver):
        self.driver=driver
    def click_on_apponitment_history(self):
        self.driver.find_element("xpath","//span[text()=' Appointment History ']").click()
    def Click_on_patient(self):
        self.driver.find_element("xpath","//span[text()=' Patients ']").click()
    def click_on_manage_patient(self):
        self.driver.find_element("xpath","//span[text()=' Manage Patient ']").click()
    def add_patient(self,name,contact,email,gender,address,age,medical_history):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(Addpatient.click_patient)
        sw.click_element(Addpatient.click_addpatient)
        sw.enter_text(Addpatient.pat_name,value=name)
        sw.enter_text(Addpatient.pat_contact,value=contact)
        sw.enter_text(Addpatient.pat_email,value=email)
        if gender.upper()=="MALE":
            sw.click_element(Addpatient.pat_gender_male)
        elif gender.upper()=="FEMALE":
            sw.click_element(Addpatient.pat_gender_female)
        sw.enter_text(Addpatient.pat_address,value=address)
        sw.enter_text(Addpatient.pat_age,value=age)
        sw.enter_text(Addpatient.pat_med_his,value=medical_history)
        sw.click_element(Addpatient.add_button)

