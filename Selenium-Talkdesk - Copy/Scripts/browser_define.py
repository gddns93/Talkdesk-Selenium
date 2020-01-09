
def create_browser():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    webdriver = webdriver.Chrome('C:\\Users\Griffin\Pycharm-Python-Projects\chromedriver.exe')

    return webdriver

browser_webdriver = create_browser() #global

