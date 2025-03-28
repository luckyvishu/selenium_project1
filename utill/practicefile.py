# from genral_utility.scrolllingfile import *
# from genral_utility.conftest import *
# from genral_utility.randomtimegenrate import *
#
#
# sw=get_date(setup_teardown)
# element=sw.generate_random_email()
# print(element)
# rtg=Randomtime(setup_teardown)
# element2=rtg.generate_random_time()
# print(element2)
# from datetime import datetime, timedelta
#
# # Get the current date
# current_date = datetime.now()
#
# # Add one day to the current date
# next_day = current_date + timedelta(days=-10)
#
# # Format the next day's date (you can adjust the format)
# next_day_str = next_day.strftime("%Y-%m-%d")  # Example: '2025-03-25'
#
# print(f"Next day's date is: {next_day_str}")
# import random
# import string
# def generate_random_email(domain="gmail.com"):
#     # Generate a random string of 10 characters (you can adjust the length)
#     random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
#
#     # Create the email by combining the random string and the domain
#     email = f"{random_string}@{domain}"
#
#     return email
#
#
# # Example usage
# random_email = generate_random_email()
# print(random_email)
#
# random_email2=generate_random_email()
# print(random_email2)
import genral_utility.scrolllingfile
# from genral_utility.scrolllingfile import get_date
#
# sw=get_date()
from xlrd import open_workbook
from xlrd import open_workbook



def get_data_from_excel():
    wb = open_workbook("C:\\Users\\QSP-USER\\PycharmProjects\\selenium_hospital_management sysytem\\AdminData-2.xls")
    sh = wb.sheet_by_name("Sheet1")
    value=sh.row_values(34, 0, 7)
    print(value[0],value[1],value[2],value[3],value[4],value[5],value[6])


get_data_from_excel()






