# homework (theme is list in python 08.08.2023)

ukrainian_cities_string = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч".replace('.', ',')
ukrainian_cities_list = ukrainian_cities_string.replace(',', ' ').title().split()

print(ukrainian_cities_list)

love_unicode = '\U00002764'

for city in ukrainian_cities_list:
    print(f'Я {love_unicode} {city}')
