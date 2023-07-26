from library.data_helper import *
from library.basic_selenium_actions import *
from constants.xpaths.raman import *
import time

def switch_to_admin_page(driver):
    print("Switching the automation project")
    #data = read_csv_data("constants/data/login_creds.csv")
    #driver = open_browser("https://tsqa1.admin.raman.devzinier.net")
    # wait_until_element_is_visible(driver,nav_button)
    # click_element(driver,nav_button)
    # wait_until_element_is_visible(driver,lst_Admin)
    # click_element(driver,lst_Admin)
    wait_until_element_is_visible(driver, users_option)
    click_element(driver,users_option)
    time.sleep(10)