# first typy of homework
import requests
import json

url = 'https://script.google.com/macros/s/AKfycbyM7-tk5popW6_Brb7ks9deSxjpMGlJniO2GWvMOqx3CheGVJP6J24sCZRftI0QYWtZ/exec'

data = requests.get(url)

data_dict = data.json()

with open('mygoogledata.json', mode='w', encoding='utf-8') as file:
    json.dump(data_dict, file)

# second typy of homework
sort1 = [2, 3, 2, 3, 4, 2.2, 3.7]
result1 = map(lambda data1: str(data1), sort1)
print(list(result1))

# third typy of homework
sort2 = [2.21, 1.1, 1.2, 1, 2, 3, 4, 5]


def sort_int_numbers(value):
    return type(value) == int


result2 = filter(sort_int_numbers, sort2)
print(list(result2))
