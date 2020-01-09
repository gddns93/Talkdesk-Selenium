import get_creds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('C:\\Users\Griffin\Pycharm-Python-Projects\chromedriver.exe')
browser.get("https://better.okta.com")




# Login to Okta






okta_username_field = browser.find_element_by_id('okta-signin-username')
okta_password_field = browser.find_element_by_id('okta-signin-password')
okta_signin = browser.find_element_by_id('okta-signin-submit')

okta_username_field.send_keys(get_creds.okta_username)
okta_password_field.send_keys(get_creds.okta_password)
okta_signin.click()