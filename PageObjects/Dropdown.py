from selenium.webdriver.common.by import By


class All_elements:
    def __init__(self, driver):
        self.driver = driver

    # fetching all the subject and checking with database

    list_subject=(By.XPATH,"//div[@id='slicer-dropdown-popup-96908df2-37fa-ab0b-521d-7c54b689a46d']/div/div[1]/div[2]/div/div/div/div/div/div/span")

    def all_subject(self):
         return  self.driver.find_elements(*All_elements.list_subject)
