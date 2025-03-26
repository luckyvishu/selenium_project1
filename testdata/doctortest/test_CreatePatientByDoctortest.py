from objectrepository.HomePage import *
from objectrepository.DoctorLoginPage import *
from objectrepository.AddPatientPage import *
from genral_utility.scrolllingfile import *
from genral_utility.conftest import *
from time import sleep
from objectrepository.LogoutPage import *

def test_Createpatientbydoctortest(setup_teardown):
    hp = home_page(setup_teardown)
    hp.click_logins_button()
    hp.click_doctor_loginbutton()
    allwindow = hp.driver.window_handles
    hp.driver.switch_to.window(allwindow[1])
    dlp = Login(setup_teardown)
    sf = get_date(setup_teardown)
    doc_det=sf.get_data_from_excel(45,0,2)
    dlp.login(doc_det[0],doc_det[1])
    app=Addpatient(setup_teardown)
    patdet=sf.get_data_from_excel(47,0,7)
    patent_email_id = patdet[2]
    run_time_email_id = patent_email_id.replace("@", (str(sf.gen_random_number()) + "@"))
    app.add_patient(patdet[0],patdet[1],run_time_email_id,"male",patdet[3],patdet[4],patdet[5])
    lo = logout(setup_teardown)
    lo.Logout()
