import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com/contact")
    # send keys events
    send_keys_to_element(driver.find_element(By.NAME, "firstname"), "Tosbabe")
    send_keys_to_element(driver.find_element(By.NAME, "lastname"), "Gbagbe")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "hello@gmail.com")
    send_keys_to_element(driver.find_element(By.NAME, "phone"), Keys.CONTROL, "v")
    send_keys_to_element(driver.find_element(By.NAME, "message"), "Hello Test Automation Engineers")
    # Click/Mouse events
    form = driver.find_element(By.TAG_NAME, "form")
    form.find_element(By.TAG_NAME, "button").click()
    form.find_element(By.XPATH, '//*[@id="Partnership"]').click()
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()