# homework (Theme is 'set' in python)

benevolent_cities_in_which_he_was = input('Enter the cities you have visited in the last 10 years: ').title().split()
future_cities = input('Enter the cities you would like to visit in the next 10 years: ').title().split()

set1_cities = set(benevolent_cities_in_which_he_was)
set2_cities = set(future_cities)

set3_cities = set1_cities & set2_cities

if set3_cities:
    cities = ', '.join(set3_cities)
    print(f'You probably liked: {cities}!!!')
else:
    print("It's cool that you want to visit other cities")
