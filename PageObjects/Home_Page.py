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

    InstitueDropdown =(By.XPATH,"//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[13]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div/i")

    def Institue(self):
        return self.driver.find_element(*HomePage.InstitueDropdown)

    InstituteName=(By.XPATH,"//span[@title='G P Mumbai']")
    def InstituteName1(self):
        return self.driver.find_element(*HomePage.InstituteName)
    # chcekbox for G.P.Mumbai isntitue
    institutecheckbox=(By.XPATH,"//div[@class='row'][2]/div")
    def checkbox(self):
        return self.driver.find_element(*HomePage.institutecheckbox)
    # to select the institue name slicier.
    slicier= (By.XPATH,"//span[text()='G P Mumbai']/ancestor::div[contains(@class, 'slicerItemContainer')]")
    def slicier1(self):
        return self.driver.find_element(*HomePage.slicier)
    # --------------Selecting second dropdown of COURSE --------------------------------
    # to select the course drop down
    CourseDropdown=(By.XPATH,"//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[15]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div/i")
    def CourseDropdown1(self):
        return self.driver.find_element(*HomePage.CourseDropdown)
    # xpath for slicier of computer engineering
    comslicier=(By.XPATH,"//span[text()='Computer Engineering']/ancestor::div[contains(@class, 'slicerItemContainer')]")
    def slicier2(self):
        return self.driver.find_element(*HomePage.comslicier)

    # ---------------Selecting the semester dropdown-----------------
    SemesterDropdown=(By.XPATH,"//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[14]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div/i")
    def Semdropdown(self):
        return self.driver.find_element(*HomePage.SemesterDropdown)
    #XPATH FOR THE SLICIER OF Semester1
    semslicier3=(By.XPATH,"//span[text()='Semester 1']/ancestor::div[contains(@class, 'slicerItemContainer')]")
    def slicier3(self):
        return self.driver.find_element(*HomePage.semslicier3)
    #---------selecting Subject from dropdown---------------------------

    SubjectDropdown=(By.XPATH,"//div[@class='slicer-dropdown-menu' and @aria-label='Subject_name']/i")
    def Subjectdropdown(self):
        return self.driver.find_element(*HomePage.SubjectDropdown)
    #Xpath for the Engineering Drawing
    subjectslicier4=(By.XPATH,"//span[text()='Engineering Drawing']/ancestor::div[contains(@class, 'slicerItemContainer')]")
    def slicier4(self):
        return self.driver.find_element(*HomePage.subjectslicier4)




