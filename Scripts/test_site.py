import browser_define
from browser_define import browser_webdriver
import new_user
from new_user import user_details

browser_webdriver.get(
    'https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')  # Opens specified website
browser_webdriver.find_elements_by_id('display-name')

#left off trying to move display name value to send keys

class SiteElements:

    def __init__(self):
        self.display_name_id = browser_webdriver.find_elements_by_id('display-name')
        self.email_field_id = browser_webdriver.find_element_by_id('email')

        return self, display_name_id

    def sdn(self):

        SiteElements.display_name_id.send_keys('test')

        return self.display_name_id

input_field_obj = SiteElements()

input_field_obj.sdn()

# print input_field_obj.sdn()



field_id = SiteElements

# input_email = send_keys(user_details.email)


# print(field_id.set_display_name())

# form_input = SiteElements()
#
#     def input_data(form_input)
#
#       return form_input


# form_input.set_site_elements()
#
# form_input.display_name_id.send_keys(user_details.name)


# class Site_Elements:
#
#     def __init__(self, display_name_field, email_field):
#
#         self.display_name_field = display_name_field
#         self.email_field = email_field


# print(Site_Elements.form_interaction(form_input))


#

# self.signup.send_keys(#left click))
