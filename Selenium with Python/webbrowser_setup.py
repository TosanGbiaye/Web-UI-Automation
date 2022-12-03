from selenium import webdriver
import chromedriver_autoinstaller

def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://www.google.org")
    driver.quit()
    
if __name__ == '__main__':
    main()
