from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # fetching title of the Webpage.
    TitleString = (By.XPATH, "//visual-container[@class='visual-container-component ng-star-inserted'][5]/transform/div/div[2]/div/visual-modern/div/div/div/p/span")
    def Title(self):
        return self.driver.find_element(*HomePage.TitleString)

    #Header data validation
    imageBag = (By.XPATH, "(//div[@class='imageBackground'])[3]")

    def imageBag1(self):
        return self.driver.find_element(*HomePage.imageBag)

   #DropDown List
    dropDownList=(By.XPATH, "(//div[@class='imageBackground'])[3]")




