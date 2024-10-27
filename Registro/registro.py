from Util.wait_web import send_keys, click, clear_send_keys, clear, text
import POM.registro_page
import datetime
from selenium.webdriver.common.keys import Keys


def registro(driver):
    print(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Logging into the page")
    POM.registro_page.navigate_url(driver)
    send_keys(driver, POM.registro_page.FirstName, 'Teste')
    send_keys(driver, POM.registro_page.LastName, 'Teste')
    send_keys(driver, POM.registro_page.Email, 'Teste@gmail.com')
    click(driver, POM.registro_page.Male)
    send_keys(driver, POM.registro_page.Mobile, '1234567891')
    # click(driver, POM.registro_page.Date)
    # clear_send_keys(driver, POM.registro_page.Date, '08/05/2005')
    #send_keys(driver, POM.registro_page.Date, '08/05/2005')

    #click(driver, POM.registro_page.Day5)
    #click(driver, POM.registro_page.Month5)
    #click(driver, POM.registro_page.Year2005)
    click(driver, POM.registro_page.Sports)
    # click(driver, POM.registro_page.State)
    # text(driver, POM.registro_page.State, 'NCR')

    # send_keys(driver, POM.registro_page.City, 'Delhi')
    click(driver, POM.registro_page.Submit)









    
    




    # send_keys(driver, POM.GestaoXRH.login_page.Password, senha)

    # click(driver, POM.GestaoXRH.login_page.BtnLogin)


