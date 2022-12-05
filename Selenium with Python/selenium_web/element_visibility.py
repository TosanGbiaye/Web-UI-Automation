import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com/contact")
    form = driver.find_element(By.TAG_NAME, "form")
    print("form state:", form.is_displayed(), form.is_enabled())
    submit_button = form.find_element(By.TAG_NAME, "button")
    print("submit button state:", submit_button.is_displayed(), submit_button.is_enabled())
    if submit_button.is_displayed():
        print("Clicking 1")
        submit_button.click()
    time.sleep(3)

if __name__ == '__main__':
    main()