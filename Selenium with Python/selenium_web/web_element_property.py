import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def print_element_properties(element):
    print("Checked state:", element.get_property("checked"))


def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.w3.org/WAI/ARIA/apg/example-index/checkbox/checkbox-mixed")
    lettuce_checkbox = driver.find_element(By.ID, "cond1")
    tomato_checkbox = driver.find_element(By.ID, "cond2")
    mustard_checkbox = driver.find_element(By.ID, "cond3")
    sprouts_checkbox = driver.find_element(By.ID, "cond4")
    print_element_properties(lettuce_checkbox)
    print_element_properties(mustard_checkbox)
    print_element_properties(tomato_checkbox)
    print_element_properties(sprouts_checkbox)

    time.sleep(10)
    driver.quit()

if __name__ == '__main__':
    main()