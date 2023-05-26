from selenium.webdriver.common.by import By


class monthAttendence:
    def __init__(self, driver):
        self.driver = driver

    # fetching title of the Webpage.
    months_list = (By.CSS_SELECTOR,"svg[name$='Line and stacked column chart'] text[class='setFocusRing']")
    def month_dash(self):
        return self.driver.find_elements(*monthAttendence.months_list)
    # ---------------------------------------------------------------------

    attendance = (By.CSS_SELECTOR,"svg[name$='Line and stacked column chart'] text[class='label']")
    def attendance1(self):
        return self.driver.find_elements(*monthAttendence.attendance)


    # summmery report locator

    summery =(By.CSS_SELECTOR, "div.visual.visual-card.customPadding.allow-deferred-rendering svg tspan")
    def tSmryList(self):
        return self.driver.find_elements(*monthAttendence.summery)

    # iframe for characteristics
    iframe=(By.CSS_SELECTOR, "iframe[class=visual-sandbox]")
    def iframe1(self):
        return self.driver.find_element(*monthAttendence.iframe)

    charList=(By.CSS_SELECTOR, "div[id=sandbox-host] g[class=word] text:nth-of-type(1)")
    # CHARACTERISTICS  FROM DASHBOARD
    def charlist1(self):
        return self.driver.find_elements(*monthAttendence.charList)


    # for the grid elements
    gridList=(By.CSS_SELECTOR, "div[role=columnheader]")

    def gridList1(self):
        return  self.driver.find_elements(*monthAttendence.gridList)

    # "-----------------------------attendence reason--------------------------"
    absentReasonList=(By.CSS_SELECTOR,"svg[name='Stacked bar chart'] text[class='setFocusRing']")

    def absentReasonList1(self):
        return self.driver.find_elements(*monthAttendence.absentReasonList)

    absentPerList=(By.CSS_SELECTOR, "svg[name='Stacked bar chart'] text[class='label']")

    def absentPerList1(self):
        return self.driver.find_elements(*monthAttendence.absentPerList)