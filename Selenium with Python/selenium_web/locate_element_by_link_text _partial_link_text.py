import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def locate_by_link_text(driver):
    academy_link = driver.find_element(By.LINK_TEXT, "Academy")
    print("Academy link element:", academy_link)
    hire_link = driver.find_element(By.LINK_TEXT, "Hire")
    print("Hire link:", hire_link)

def locate_by_partial_link_text(driver):
    academy_link = driver.find_element(By.PARTIAL_LINK_TEXT, "adem")
    print("Academy link|partial|:", academy_link)
    test_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Test")
    print("Total Test links:", len(test_links))
    for test_link in test_links:
        print("A Test link:", test_link)




def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com")
    locate_by_partial_link_text(driver)
    time.sleep(3)
    driver.quit()



if __name__ == '__main__':
    main()