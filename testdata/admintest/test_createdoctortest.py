from objectrepository.HomePage import *
from objectrepository.AddDoctor import *
from objectrepository.AddPatientPage import *
from objectrepository.DoctorLoginPage import *
from objectrepository.AdminLoginPage import *
from objectrepository.LogoutPage import *
from genral_utility.conftest import *
from genral_utility.scrolllingfile import *

def test_create_doctor_test(setup_teardown):
    hp=home_page(setup_teardown)
    al=Loginasadmin(setup_teardown)
    hp.click_logins_button()
    hp.click_admin_loginbutton()
    allwindow=al.driver.window_handles
    al.driver.switch_to.window(allwindow[1])
    sf = get_date(setup_teardown)
    admin_credential = sf.get_data_from_excel(30, 0, 2)
    al.admin_login(admin_credential[0], admin_credential[1])
    ad=Adddoctor(setup_teardown)
    docdet = sf.get_data_from_excel(34, 0, 7)
    doc_mail_id = docdet[6].replace("@", (str(sf.gen_random_number()) + "@"))
    ad.add_Docotor(docdet[0], docdet[1], docdet[2], str(int(docdet[3])), doc_mail_id, docdet[4], docdet[5])
    lo=logout(setup_teardown)
    lo.Logout()
    hp.click_logins_button()
    hp.click_doctor_loginbutton()
    allwindow = al.driver.window_handles
    al.driver.switch_to.window(allwindow[2])
    li=Login(setup_teardown)
    li.login(doc_mail_id,docdet[4])
    adp=Addpatient(setup_teardown)
    patdet = sf.get_data_from_excel(47, 0, 7)
    pat_mail_id = patdet[2].replace("@", (str(sf.gen_random_number()) + "@"))
    adp.add_patient(patdet[0], patdet[1], pat_mail_id, "male", patdet[3], patdet[4], patdet[5])
    sleep(2)
    adp.Click_on_patient()
    sleep(1)
    adp.click_on_manage_patient()
    lo.Logout()














