from genral_utility.lib import SeleniumWrapper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class create_patient:
    fullname=("xpath","//input[@name='full_name']")
    address=("xpath","//input[@name='address']")
    city=("xpath","//input[@name='city']")
    gender_female=("xpath","//label[contains(text(),'Female')]")
    gender_male=("xpath","//label[contains(text(),'Male')]")
    email=("xpath","//input[@name='email']")
    password=("xpath","//input[@name='password']")
    again_password=("xpath","//input[@name='password_again']")
    submit_btn=("xpath","//button[@name='submit']")

    def __init__(self,driver):
        self.driver=driver
    def Login_link(self):
        self.driver.find_element(self.login_link).click()
    def Create_patient(self,fullname,address,city,gender,email,password,again_password):
        sw=SeleniumWrapper(self.driver)
        sw.enter_text(create_patient.fullname,value=fullname)
        sw.enter_text(create_patient.address,value=address)
        sw.enter_text(create_patient.city,value=city)
        if gender.upper()=='MALE':
            sw.click_element(create_patient.gender_male)
        elif gender.upper=='FEMALE':
            sw.click_element(create_patient.gender_female)
        sw.enter_text(create_patient.email,value=email)
        sw.enter_text(create_patient.password,value=password)
        sw.enter_text(create_patient.again_password,value=again_password)
        self.driver.execute_script(f"window.scrollBy(0, 1700)")
        wait = WebDriverWait(self.driver, 10)
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Submit')]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_button).click().perform()
        self.driver.switch_to.alert.accept()
