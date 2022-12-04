import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com/contact")
    email_inputs = driver.find_elements(By.NAME, "email")
    print("Found:", len(email_inputs), "email input")
    # form
    first_form = driver.find_element(By.TAG_NAME, "form")
    contact_us_form_email_input = first_form.find_elements(By.NAME, "email")
    print("form found:", len(contact_us_form_email_input))
    time.sleep(3)
    driver.quit()



if __name__ == '__main__':
    main()