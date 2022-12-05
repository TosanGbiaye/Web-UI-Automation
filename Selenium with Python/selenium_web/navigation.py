import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.testifyltd.com/contact")
    time.sleep(2)
    driver.refresh()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "About us").click()
    time.sleep(3)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    main()