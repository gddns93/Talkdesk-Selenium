import browser_define
from browser_define import browser_webdriver
import new_user
from new_user import user_details

browser_webdriver.get('https://better.mytalkdesk.com/#admin/agents/new')  # Opens specified website

class SiteElements:

def __init__(self):

    self.save = browser.find_element_by_name('save')
    self.name = browser.find_element_by_id('name')
    self.email = browser.find_element_by_id('email')
    self.ringgroup = browser.find_element_by_name('tags')

    return self


self.name.send_keys(user_details.name)
self.email.send_keys(user_details.email)
self.ringgroup.send_keys(user_details.ringgroup)





