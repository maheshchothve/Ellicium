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

    InstitueDropdown =(By.XPATH,"//div[@class='slicer-dropdown-menu' and @aria-label='Institute_name']/i")

    def Institue(self):
        return self.driver.find_element(*HomePage.InstitueDropdown)
    checkbox=(By.XPATH,"//span[@title='G P Mumbai']")

    def checkbox_list(self):
        return self.driver.find_element(*HomePage.checkbox)


        # --------------Selecting second dropdown of COURSE --------------------------------
    # to select the course drop down
    CourseDropdown=(By.XPATH,"//div[@class='slicer-dropdown-menu' and @aria-label='Course_name']/i")
    def CourseDropdown1(self):
        return self.driver.find_element(*HomePage.CourseDropdown)

    Course_checkbox=(By.XPATH,"//*[@id='slicer-dropdown-popup-9d48dd6c-51f8-e265-5be2-3a24acd2b838']/div[1]/div/div[2]/div/div[1]/div/div/div/div/span")
    def Course_checkbox1(self):
        return self.driver.find_elements(*HomePage.Course_checkbox)

    # ---------------Selecting the semester dropdown-----------------
    SemesterDropdown=(By.XPATH,"//div[@class='slicer-dropdown-menu' and @aria-label='semester']/i")
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
        return self.driver.find_elements(*HomePage.subjectslicier4)





