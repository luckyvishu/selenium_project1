

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
#from test_createdoctortest import *
#from test_patienttest import *
import pytest
from time import sleep

@pytest.fixture(scope="function")
def setup_teardown():

    chrome_options = Options()
    chrome_options.add_experimental_option(name='detach', value=True)
    driver = WebDriver(chrome_options)
    driver.maximize_window()
    sleep(2)
    driver.get("http://49.249.28.218:8081/AppServer/Hospital_Doctor_Patient_Management_System/")
    sleep(2)
    yield driver
    driver.quit()


