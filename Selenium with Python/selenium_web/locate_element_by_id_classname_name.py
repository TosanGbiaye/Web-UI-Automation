import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service 
from webdriver_manager.chrome import ChromeDriverManager

def locate_by_id(driver):
    email_element = driver.find_element(By.ID, "email")
    print("Email Element:", email_element)
    password_element = driver.find_element(By.ID, "pass")
    print("Password Element:", password_element)


def locate_by_name(driver):
    firstname_element = driver.find_element(By.NAME, "firstname")
    print("Firstname Element:", firstname_element)
    lastname_element = driver.find_element(By.NAME, "lastname")
    print("Lastname Element:", lastname_element)

def locate_by_class_name(driver):
    rr_firstelement = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("React reveal first Element:", rr_firstelement)
    # To find elements in a webpage
    rr_elements = driver.find_elements(By.CLASS_NAME, "react-reveal")
    for rr_element in rr_elements:
        print("React reveal Element:", rr_elements)



def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # driver.get("https://web.facebook.com")    # used to find element by id
    # locate_by_id(driver)
    driver.get("https://www.testifyltd.com/contact")   # used to find element by name
    # locate_by_name(driver)
    locate_by_class_name(driver)
    time.sleep(3)
    driver.quit()



if __name__ == '__main__':
    main()