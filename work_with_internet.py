from pywebio.output import put_success
import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url=url)

result = response.json()

people = result['people']

list_of_astronauts = []

for person in people:
    list_of_astronauts.append(person['name'])

put_success(f'{list_of_astronauts} , astronauts who are currently in space \U0001F6F0')
