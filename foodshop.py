import requests

url = 'https://script.google.com/macros/s/AKfycbyM7-tk5popW6_Brb7ks9deSxjpMGlJniO2GWvMOqx3CheGVJP6J24sCZRftI0QYWtZ/exec'

data = requests.get(url)

data_dict = data.json()

total_cost = sum([product["price"] * product["remainder"] for product in data_dict['shop']])
total_cost_without_gluten = sum([product["price"] * product["remainder"] for product in data_dict['shop'] if not product["contains_gluten"]])

print(f"Сума всіх товарів складає {total_cost} гривень.")
print(f"Сума товарів без глютену складає {total_cost_without_gluten} гривень.")
