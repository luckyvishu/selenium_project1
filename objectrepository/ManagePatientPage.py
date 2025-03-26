

class managepatientpage:
    managepatient=("xpath","//span[text()=' Manage Patient ']")
    def __init__(self,driver):
        self.driver=driver
    def ManagePatient(self):
        element=self.driver.find_element("xpath","//span[text()=' Manage Patient ']")
        return element

