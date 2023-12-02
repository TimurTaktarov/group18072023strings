import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'

params = {
    'limit': 150,
    'skip': 0,
}

response = requests.get(url=url, params=params)

result = response.json()

todos = result['todos']

for todo in todos:
    todo['smile'] = ':)'
    if todo['completed'] is False:
        todo['smile'] = ':('
        print('*' * 10)
        print(f' {todo["id"]} {todo["completed"]} {todo["smile"]}')
