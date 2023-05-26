import time

from selenium.webdriver.common.by import By

from Utility.DatabaseUtility import DatabaseConnection

class dropdown():

    def dropDownSelection(driver, dropDownList, expVal, dropDownName):
        for i in range(1, len(dropDownList) + 1):
            name = driver.find_element(By.XPATH,
                                   "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(
                                       i) + "]")
            nameSel = driver.find_element(By.XPATH,
                                      "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(
                                          i) + "]/preceding-sibling::div")

            print("Name: " + name.text)
            print("NameSel: " + nameSel.get_attribute("class"))
            if name.text == expVal:
                if nameSel.get_attribute("class") != "slicerCheckbox selected":
                    name.click()
                    print("Selected " + expVal)
                    break
                else:
                    print("Already Selected " + expVal)


    def get_dropdown_values(driver, dropdown_name, expected_value):
        time.sleep(3)
        dropdown_xpath = "//div[@class='slicer-dropdown-menu' and @aria-label='" + dropdown_name + "']/i"
        driver.find_element(By.XPATH, dropdown_xpath).click()
        time.sleep(5)

        dropdown_list = driver.find_elements(By.XPATH,
                                         "//div[@class='slicerBody' and @aria-label='" + dropdown_name + "']//div[@class='slicerItemContainer']/span")
        dropdown.dropDownSelection(driver, dropdown_list, expected_value, dropdown_name)

        dropdown_values = []
        for item in dropdown_list:
            dropdown_values.append(item.text)
    #   print("Dashboard", dropdown_name, "names are", dropdown_values)
        return dropdown_values


    def compare_dashboard_database(driver,dropdown_name,dashboard_values,database_query):
            print(f"{dropdown_name} from dashboard are{dashboard_values}")
            obj = DatabaseConnection
            database_values = obj.Query(driver, database_query)
            print(f"{dropdown_name} from database values are{database_values}")
            database_values = [name[0] for name in database_values]
        # Compare the lists
            if set(database_values) == set(dashboard_values):
                 print("The lists match.")
            else:
                print("The lists do not match.")
