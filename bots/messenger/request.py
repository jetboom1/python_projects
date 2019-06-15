import requests
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()
new_user = {
    'name':'John',
    'last_name':'Doe',
    'email':'johndoe@example.com'
}
test = requests.post('https://jsonplaceholder.typicode.com/users', new_user)
print(test.content)