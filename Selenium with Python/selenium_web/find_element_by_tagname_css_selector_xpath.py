import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def locate_by_tag_name(driver):
    first_input_element = driver.find_element(By.TAG_NAME, "input")
    print("First input Element:", first_input_element)
    # To find multiple elements for instance to find all the divs in the webpage execute the below command:
    div_elements = driver.find_elements(By.TAG_NAME, "div")
    print("Total div:", len(div_elements))
    for div_element in div_elements:
        print("Div Elements:", div_element)


def locate_by_css_selector(driver):
    firstname_element = driver.find_element(By.CSS_SELECTOR, "#__next > main > section.relative.bg-primary.contact-section > div > div.mt-12.lg\:mt-16.w-full.xl\:w-11\/12.mx-auto.flex.flex-row.flex-wrap.items-start > div.w-full.md\:w-8\/12.bg-white.px-5.md\:px-8.xl\:px-12.pt-12.pb-14 > form > div:nth-child(1) > div:nth-child(1) > input")
    print("Firstname Element by CSS Selector:", firstname_element)
    div_elements = driver.find_elements(By.CSS_SELECTOR, "div.relative")
    print("Total div.relative elements:", len(div_elements))
    for div_element in div_elements:
        print("div.relative element:", div_element)
def locate_by_xpath(driver):
    firstname_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[1]/div[1]/input')
    print("firstname element by xpath:", firstname_element)
    form = driver.find_element(By.XPATH, "//form[1]")
    print("form element: ", form)


def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com/contact")   # used to find element by name
    #locate_by_tag_name(driver)
    #locate_by_css_selector(driver)
    locate_by_xpath(driver)

    time.sleep(3)
    driver.quit()



if __name__ == '__main__':
    main()