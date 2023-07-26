from library.data_helper import *
from library.basic_selenium_actions import *
from constants.xpaths.raman import *
import time

def login():
    print("Starting the automation project")
    data = read_csv_data("constants/data/login_creds.csv")
    driver = open_browser("https://tsqa1.admin.raman.devzinier.net")
    wait_until_element_is_visible(driver,txt_box_email)
    wait_until_element_is_visible(driver,txt_box_password)
    enter_text_in_element(driver,txt_box_email,data[0]['usr_nm'])
    enter_text_in_element(driver,txt_box_password,data[0]['pwd'])
    click_element(driver,btn_login)
    wait_until_element_is_visible(driver, znr_logo)
    time.sleep(10)
    return driver



