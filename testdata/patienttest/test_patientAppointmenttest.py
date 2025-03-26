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
    sleep(1)
    lp.Create_Link()
    cp=create_patient(setup_teardown)
    pei=get_date(setup_teardown)
    patdet=pei.get_data_from_excel(3,0,6)
    patent_email_id=patdet[4]
    run_time_email_id=patent_email_id.replace("@",(str(pei.gen_random_number())+"@"))
    cp.Create_patient(patdet[0],patdet[1],patdet[2],patdet[3],run_time_email_id,patdet[5],patdet[5])
    sleep(1)
    lp.driver.execute_script(f"window.scrollBy(0, 1700)")
    sleep(1)
    lp.Login_link()
    lp.login_patient(run_time_email_id,patdet[5])
    sleep(1)
    ba = Bookappointment(setup_teardown)
    ba.Book_appointment(3)
    sleep(1)
    ba.driver.switch_to.alert.accept()
    sleep(1)
    lo = logout(setup_teardown)
    lo.Logout()
    hp.click_logins_button()
    hp.click_doctor_loginbutton()
    allwindow = lp.driver.window_handles
    lp.driver.switch_to.window(allwindow[2])
    sleep(2)
    dl=Login(setup_teardown)
    doc_det = pei.get_data_from_excel(45, 0, 2)
    dl.login(doc_det[0], doc_det[1])
    sleep(2)
    ap=Addpatient(setup_teardown)
    ap.click_on_apponitment_history()
    lo.Logout()









