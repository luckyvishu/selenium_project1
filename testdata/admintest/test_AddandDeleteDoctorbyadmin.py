from objectrepository.HomePage import *
from objectrepository.AddDoctor import *
from objectrepository.AdminLoginPage import *
from objectrepository.DeleteDoctorPage import *
from objectrepository.LogoutPage import *
from genral_utility.scrolllingfile import *
from genral_utility.conftest import *
from time import sleep
import time

def test_Add_and_Delete_doctor_by_admin(setup_teardown):
    hp=home_page(setup_teardown)
    hp.click_logins_button()
    hp.click_admin_loginbutton()
    al =Loginasadmin(setup_teardown)



    allwindow = al.driver.window_handles
    al.driver.switch_to.window(allwindow[1])
    sf = get_date(setup_teardown)
    admin_credential=sf.get_data_from_excel(30,0,2)

    al.admin_login(admin_credential[0], admin_credential[1])
    ad = Adddoctor(setup_teardown)

    docdet = sf.get_data_from_excel(34,0,7)
    doc_mail_id=docdet[6].replace("@",(str(sf.gen_random_number())+"@"))
    doctor_name = (docdet[0]+str(sf.gen_random_number()))
    ad.add_Docotor(doctor_name, docdet[1], docdet[2], str(int(docdet[3])), doc_mail_id, docdet[4], docdet[5])

    ddp=Deletedocotrpage(setup_teardown)
    ddp.Deletedoctor()
    sf.scroll_up()
    sleep(1)
    ad.driver.find_element("xpath","//td[text()='"+ f'{doctor_name}'+"']/following-sibling::td//i[@class='fa fa-times fa fa-white']").click()
    sf.switchtoalertAccept()

    delete_message=ddp.getDeletedmessage()
    if delete_message == "data deleted !!":#(f"Expected 'data delete !!', but got {delete_message}":)
        assert True
    else:
        sf.take_screenshot()

        assert False




