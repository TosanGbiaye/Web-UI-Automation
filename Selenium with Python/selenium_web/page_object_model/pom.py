import time
from selenium import webdriver
from ContactPage import ContactPage
from AboutUsPage import AboutUsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/contact")
    contact_page = ContactPage(driver)
    about_us_page = AboutUsPage(driver)
    print(contact_page.firstname_input, contact_page.lastname_input)
    contact_page.submit_button.click()
    print(about_us_page.title.text)
    time.sleep(20)

if __name__ == '__main__':
    main()