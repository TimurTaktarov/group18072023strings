class Car:
    def __init__(self, producer: str, brand: str, fuel_consumption: float, graduation_year: int = 2020):
        self.graduation_year = graduation_year
        self.producer = producer
        self.brand = brand
        self.run = 0
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'Сharacteristic of the car: ↓' \
               f'\n graduation year: {self.graduation_year}' \
               f'\n producer: {self.producer}' \
               f'\n brand: {self.brand}' \
               f'\n run: {self.run}' \
               f'\n fuel_consumption: {self.fuel_consumption}'


auto = Car(producer='BMW', brand="Rolls-Royce", fuel_consumption=15.2)
auto2 = Car(producer='Volkswagen', brand="Porsche", fuel_consumption=10.9, graduation_year=2077)
auto3 = Car(producer='Toyota', brand="Lexus", fuel_consumption=16.8, graduation_year=2023)
print(auto)
print(auto2)
print(auto3)
