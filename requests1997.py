import requests

url = 'https://dummyjson.com/todos'

params = {
    'limit': 150,
    'skip': 0,
}

response = requests.get(url=url, params=params)

result = response.json()

tod = result['todos']

for todo in tod:
    if todo['completed'] is False:
        print('*' * 10)
        print(todo)
