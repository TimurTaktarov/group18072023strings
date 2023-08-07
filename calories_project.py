from pywebio.input import input as pw_input
from pywebio.input import FLOAT
from pywebio.output import put_success, put_warning, toast
from decimal import Decimal

# price of the 1 calorie
price_one_calorie = 0.32541

# on 100 gram
OSTRICH_EGG = 118
RABBIT = 197
SEA_PERCH = 123
RED_SWEET_PEPPER = 26
PARSLEY = 45
BANANAS = 87
WAFFLES = 425
WHEAT_BREAD = 246
PISTACHOS = 555
KEFIR_TWO_AND_HALF_INTEREST = 51

egg_unicode = '\U0001F373'
bunny_unicode = '\U0001F407'
perch_unicode = '\U0001F41F'
pepper_unicode = '\U0001F336'
parsley_unicode = '\U0001F96C'
banana_unicode = '\U0001F34C'
waffle_unicode = '\U0001F9C7'
bread_unicode = '\U0001F35E'
pistachos_unicode = '\U0001F95C'
kefir_unicode = '\U0001F95B'
money_unicode = '\U0001F911'
yummy_unicode = '\U0001F60B'

total_calories = 0

EGG_USER_DATA = pw_input("Enter how much grams ostrich egg you need", type=FLOAT, required=True)
portion1 = EGG_USER_DATA * OSTRICH_EGG / 100
total_calories = portion1 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion1} {egg_unicode}')

BUNNY_USER_DATA = pw_input("Enter how much grams rabbit you need", type=FLOAT, required=True)
portion2 = BUNNY_USER_DATA * RABBIT / 100
total_calories = portion2 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion2} {bunny_unicode}')

PERCH_USER_DATA = pw_input("Enter how much grams sea perch you need", type=FLOAT, required=True)
portion3 = PERCH_USER_DATA * SEA_PERCH / 100
total_calories = portion3 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion3} {perch_unicode}')

PEPPER_USER_DATA = pw_input("Enter how much grams red sweet pepper you need", type=FLOAT, required=True)
portion4 = PEPPER_USER_DATA * RED_SWEET_PEPPER / 100
total_calories = portion4 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion4} {pepper_unicode}')

PARSLEY_USER_DATA = pw_input("Enter how much grams parsley you need", type=FLOAT, required=True)
portion5 = PARSLEY_USER_DATA * PARSLEY / 100
total_calories = portion5 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion5} {parsley_unicode}')

BANANA_USER_DATA = pw_input("Enter how much grams bananas you need", type=FLOAT, required=True)
portion6 = BANANA_USER_DATA * BANANAS / 100
total_calories = portion6 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion6} {banana_unicode}')

WAFFLE_USER_DATA = pw_input("Enter how much grams waffles you need", type=FLOAT, required=True)
portion7 = WAFFLE_USER_DATA * WAFFLES / 100
total_calories = portion7 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion7} {waffle_unicode}')

BREAD_USER_DATA = pw_input("Enter how much grams wheat bread you need", type=FLOAT, required=True)
portion8 = BREAD_USER_DATA * WHEAT_BREAD / 100
total_calories = portion8 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion8} {bread_unicode}')

PISTACHOS_USER_DATA = pw_input("Enter how much grams pistachos you need", type=FLOAT, required=True)
portion9 = PISTACHOS_USER_DATA * PISTACHOS / 100
total_calories = portion9 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion9} {pistachos_unicode}')

KEFIR_USER_DATA = pw_input("Enter how much grams kefir you need", type=FLOAT, required=True)
portion10 = KEFIR_USER_DATA * KEFIR_TWO_AND_HALF_INTEREST / 100
total_calories = portion10 + total_calories
put_success(f'Full calorie content of order: {total_calories}, product calorie content: {portion10} {kefir_unicode}')

if total_calories < 1000:
    put_warning("You will be hungry, you need to eat more!")
elif total_calories < 1500:
    put_success("This is the perfect dinner option!")
    toast(f'Bon appetit! {yummy_unicode}')
else:
    put_warning("Do you want to be obese? You need to eat less food!")

price = total_calories * price_one_calorie
cost = Decimal(str(price)).quantize(Decimal('0.01'))
put_success(f'The total cost of the order is {cost} hryvnia {money_unicode}')
