with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    data = file.readlines()
    for airport in data:
        list_of_airports = airport.split(';')
        if list_of_airports[5] == 'UA':
            print(list_of_airports[2])
