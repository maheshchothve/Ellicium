from selenium.webdriver.common.by import By


class Absent_Report:
    def __init__(self, driver):
        self.driver = driver

    # fetching title of the Webpage.
    absent_reason = (By.CSS_SELECTOR,"svg[name='Stacked bar chart'] text[class='setFocusRing']")
    def absent_reason_dash(self):
        return self.driver.find_elements(*Absent_Report.absent_reason)