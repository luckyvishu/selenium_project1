from objectrepository.PatientLoginPage import *
from objectrepository.HomePage import *
from objectrepository.UserregistrationPage import *
from objectrepository.LogoutPage import *
from objectrepository.PatientAppointmentPage import *
from objectrepository.DoctorLoginPage import *
from objectrepository.AddPatientPage import *
from genral_utility.conftest import *
from genral_utility.scrolllingfile import *

def test_patient_test(setup_teardown):
    hp=home_page(setup_teardown)
    lp=Loginpatient(setup_teardown)
    hp.click_logins_button()
    hp.click_patient_loginbutton()
    allwindow = lp.driver.window_handles
    lp.driver.switch_to.window(allwindow[1])
    sleep(2)
    lp.Create_Link()
    cp=create_patient(setup_teardown)
    pei=get_date(setup_teardown)
    patdet=pei.get_data_from_excel(3,0,7)
    patent_email_id = patdet[4]
    run_time_email_id = patent_email_id.replace("@", (str(pei.gen_random_number()) + "@"))
    cp.Create_patient(patdet[0], patdet[1], patdet[2], patdet[3], run_time_email_id, patdet[5], patdet[5])
    sleep(2)
    lp.driver.execute_script(f"window.scrollBy(0, 1700)")
    sleep(2)
    lp.Login_link()
    lp.login_patient(run_time_email_id,patdet[5])
    sleep(2)
    lo = logout(setup_teardown)
    lo.Logout()

