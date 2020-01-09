

class Employee:

    def __init__(self, name, email, ringgroup):
        self.name = name
        self.email = name + '@hoax.com'
        self.ringgroup = name

    def user_info(self):
        return self.name, self.email

user_details = Employee('TestUser', 'Testuser@hoax.com', 'TestUser')

