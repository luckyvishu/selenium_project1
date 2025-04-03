from datetime import datetime,timedelta
from random import *
import random
import string
import time
#import DatafromExcel
from xlrd import *


class get_date():
    def __init__(self,driver):
        self.driver=driver
    def get_random_date(self,no_of_days):
        self.current_date = datetime.now()#to get the current date
        self.next_day = self.current_date + timedelta(days=no_of_days)
        self.next_day_str = self.next_day.strftime("%Y-%m-%d")
        return self.next_day_str
    def get_random_time(self):
        self.hour = random.randint(1, 12)
        self.minute = random.randint(0, 59)
        self.am_pm = random.choice(["AM", "PM"])
        self.formatted_time = f"{self.hour}:{self.minute:02d} {self.am_pm}"
        return self.formatted_time
    def generate_random_email(self,domain="gmail.com"):
        # Generate a random string of 10 characters (you can adjust the length)
        self.random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

        # Create the email by combining the random string and the domain
        self.email = f"{self.random_string}@{domain}"

        return self.email
    def scroll_up(self):
        self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")
    def scroll_down(self):
        self.driver.execute_script(f"window.scrollTo(500, 0)")
    def gen_random_number(self):
        random_number=randint(0,1000)
        return random_number


    def switchtoalertAccept(self):
        self.driver.switch_to.alert.accept()
    def switchtoalertDismiss(self):
        self.driver.switch_to.alert.dismiss()
    def take_screenshot(self):
        floder = "C:\\Users\\User\\PycharmProjects\\hospital_management_system\\test_screenshots"
        time_string = time.asctime().replace(":", " ")
        file_name = floder + time_string + ".png"
        self.driver.save_screenshot(file_name)

    def get_data_from_excel(self,row,row_starting_index,ending_index):
        wb = open_workbook("C:\\Users\\User\\PycharmProjects\\hospital_management_system\\AdminData-2.xls")
        sh = wb.sheet_by_name("Sheet1")
        value = sh.row_values(row,row_starting_index,ending_index)
        return value








