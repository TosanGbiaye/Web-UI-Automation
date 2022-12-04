import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def print_element_fields(element):
    print("text:", element.text)
    print("size:", element.size)
    print("location:", element.location)
    print("tag name:", element.tag_name)
    print("accessible name:", element.accessible_name)
    print("Aria role:", element.aria_role)
    print("ID:", element.id)
    print("Rectangle:", element.rect)
def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com/contact")
    #element = driver.find_element(By.TAG_NAME, "h2")
    element = driver.find_element(By.LINK_TEXT, "Academy")
    print_element_fields(element)

    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    main()