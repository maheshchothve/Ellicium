from selenium import webdriver
from PIL import Image

def take_screenshot(driver, filename):
    driver.save_screenshot(filename)
    # screenshot = Image.open(filename)
    # screenshot.show()

