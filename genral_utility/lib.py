from selenium.webdriver.support.wait import WebDriverWait
# above syntax is used to wait the execution of a program untill the conditions become true or the particular element become visible
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from selenium.webdriver.support.select import Select
#above if if element is not visible it will throw the exception to avoid that we will use
def wait_for_element(func):
    def wrapper(*args,**kwargs):
        #here we will write the pretask or post task
        instance=args[0]# here it will take the address of the object
        locator=args[1]# here it will take the argumnets i.e locators
        _wait=WebDriverWait(instance.driver,20)#here i need to pass driver instance & time out
        v=visibility_of_element_located(locator)#here i need to pass locator
        _wait.until(v)
        func(*args,**kwargs)

    return wrapper
# we are creating the class inside this class we are declearing the all the actions in the form of functions
#
class SeleniumWrapper:
    #we are creating the constructor because we have to point towards the driver so
    def __init__(self,driver):
        self.driver=driver

    @wait_for_element
    def enter_text(self,locator,/,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)
    @wait_for_element
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @wait_for_element
    def select_element_by_value(self,locator,/,*,value):

        element =self.driver.find_element(*locator)
        s = Select(element)
        s.select_by_value(value)


