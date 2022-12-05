import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# The below function: Scroll_to_element is used to scroll down to where your desired element is
def scroll_to_element(action, element):
    action.move_to_element(element).perform()
# The below function : scroll_by_offset is used to scroll a bit up and down on a webpage.
# the - sign eg (-150) is to scroll up while the plus sign eg (150)is to scroll down
def scroll_by_offset(action, delta_y):
    action.scroll_by_amount(0, delta_y).perform()
# The below function is used to right click on an element
def right_click_context(action, element):
    scroll_to_element(action, element)
    action.context_click(element).perform()
# The below function is used to highlight on web element(s)
def highlight_element1(action, element, limit=15):
    action.drag_and_drop_by_offset(element, 0, limit)
    action.perform()

def highlight_element2(action, element, limit=15):
    action.move_to_element(element)
    action.move_by_offset(0, 10)
    action.click_and_hold(on_element=None)
    action.move_by_offset(0, 10)
    action.release(on_element=None)
    action.perform()

def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.testifyltd.com/contact")
    action = ActionChains(driver)
    # The below function: Scroll_to_element is used to scroll down to where your desired element is
    # scroll_to_element(action, driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[3]/div/div/div[3]/form/input'))
    # time.sleep(3)
    # The below function : scroll_by_offset is used to scroll a bit up and down on a webpage.
    # scroll_by_offset(action, 150)  #To scroll down
    # time.sleep(2)
    # scroll_by_offset(action, 150)  # To scroll down
    # time.sleep(2)
    # scroll_by_offset(action, -150)     #To scroll up
    # time.sleep(4)
    # The below function is used to right-click on an element
    right_click_context(action, driver.find_element(By.NAME, "firstname"))
    time.sleep(10)
    # The below function is used to highlight on web element(s)
    #highlight_element1(action, driver.find_element(By.TAG_NAME, "h2"), 50)
    #time.sleep(4)

if __name__ == '__main__':
    main()
