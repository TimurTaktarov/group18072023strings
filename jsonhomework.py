import requests
import json

url = 'https://script.google.com/macros/s/AKfycbyM7-tk5popW6_Brb7ks9deSxjpMGlJniO2GWvMOqx3CheGVJP6J24sCZRftI0QYWtZ/exec'

data = requests.get(url)

data_dict = data.json()

with open('mygoogledata.json', mode='w', encoding='utf-8') as file:
    json.dump(data_dict, file)
    map(lambda data1: str(data1), file)

with open('mygoogledata.json', mode='r', encoding='utf-8') as file:
    sort = json.load(file)
    filter(lambda data2: int(data2), sort)
