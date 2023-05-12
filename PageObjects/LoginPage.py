from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    Home_email = (By.ID, "email")

    def Enter_mail(self):
        return self.driver.find_element(*LoginPage.Home_email)

    Home_submit = (By.ID, "submitBtn")

    def Enter_submit(self):
        return self.driver.find_element(*LoginPage.Home_submit)

    Home2_password = (By.ID, "i0118")

    def password(self):
        return self.driver.find_element(*LoginPage.Home2_password)

    MS_signInAgaianPage = (By.ID, "idSIButton9")

    def MS_SigninConfButton(self):
        return self.driver.find_element(*LoginPage.MS_signInAgaianPage)

    staysignin = (By.ID, "idSIButton9")

    def staysigninpage(self):
        return self.driver.find_element(*LoginPage.staysignin)
