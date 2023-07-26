from library.data_helper import *
from library.basic_selenium_actions import *
from constants.xpaths.raman import *
import time

def switch_to_admin_page(driver):
    print("Add the automation project")
    wait_until_element_is_visible(driver, btn_new_usr)
    click_element(driver,btn_new_usr)
    wait_until_element_is_visible(driver, add_new_headder)
    
    time.sleep(10)