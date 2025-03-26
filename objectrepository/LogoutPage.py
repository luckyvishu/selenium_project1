from genral_utility.lib import SeleniumWrapper
class logout:
    profile_edt=("xpath","//span[@class='username']")
    logout_btn=("xpath","//a[contains(text(),'Log')]")
    def __init__(self,driver):
        self.driver=driver
    def Logout(self):
        sw=SeleniumWrapper(self.driver)
        sw.click_element(logout.profile_edt)
        sw.click_element(logout.logout_btn)

