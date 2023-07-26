from .login import *
from .swith_to_admin_page import *

def main():
    driver = login()
    switch_to_admin_page(driver)

main()