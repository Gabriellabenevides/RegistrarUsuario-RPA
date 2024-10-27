from selenium.webdriver.common.by import By

FirstName = ('Primeiro nome', By.ID, 'firstName')
LastName = ('Último nome', By.ID, 'lastName')
Email = ('Email', By.ID, 'userEmail')
Male = ('Male', By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label')
FeMale = ('FeMale', By.ID, 'gender-radio-2')
Other = ('Other', By.ID, 'gender-radio-3')
Mobile = ('Mobile Numer', By.ID, 'userNumber')
Date = ('Date of birth', By.ID, 'dateOfBirthInput')
Day5 = ('Day of birth', By.ID, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[7]')
#Month5 = ('Month of birth', By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[5]')
#Year2005 = ('Year of birth', By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[106]')
Sports = ('Sports', By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label')
Reading = ('Reading', By.ID, 'hobbies-checkbox-2')
Music = ('Music', By.ID, 'hobbies-checkbox-3')
State = ('State', By.XPATH, '//*[@id="state"]/div/div[1]')
City = ('City', By.XPATH, '//*[@id="city"]/div/div[1]')
Submit = ('Submit', By.ID, 'submit')
Portuguese = ('Portuguese', By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[29]/a')
Country = ('Country', By.XPATH, '//*[@id="countries"]')


def navigate_url(driver):
    driver.get("https://demoqa.com/automation-practice-form")




