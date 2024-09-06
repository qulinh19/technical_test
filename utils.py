from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_driver import wait, driver


def find_el_by_x_path(attr_name,attr_value):
    return wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[@{attr_name}='{attr_value}']")))

def click_by_x_path(attr_name,attr_value):
    find_el_by_x_path(attr_name,attr_value).click()

def input_by_x_path(attr_name,attr_value,value):
    find_el_by_x_path(attr_name,attr_value).send_keys(value)