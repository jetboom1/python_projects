import twisted
class User:
    def __init__(self, first_name0, last_name0='undefined'):
        self.first_name = first_name0
        self.last_name = last_name0

    def hello(self):
        print(f'Hello, {self.first_name}')

    def __str__(self):
        return f'user: {self.first_name} {self.last_name}'


user0 = User('John', 'Doe')
user0.hello()
print(user0.last_name)
print(str(user0))
