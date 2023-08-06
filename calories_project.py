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

unicode1 = '\U0001F373'
unicode2 = '\U0001F407'
unicode3 = '\U0001F41F'
unicode4 = '\U0001F336'
unicode5 = '\U0001F96C'
unicode6 = '\U0001F34C'
unicode7 = '\U0001F9C7'
unicode8 = '\U0001F35E'
unicode9 = '\U0001F95C'
unicode10 = '\U0001F95B'
unicode11 = '\U0001F911'
unicode12 = '\U0001F60B'

total_calories = 0

OSTRICH_EGG_USER = pw_input("Enter how much grams ostrich egg you need", type=FLOAT, required=True)
portion1 = OSTRICH_EGG_USER * OSTRICH_EGG / 100
total_calories = portion1 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion1} {unicode1}')

RABBIT_USER = pw_input("Enter how much grams rabbit you need", type=FLOAT, required=True)
portion2 = RABBIT_USER * RABBIT / 100
total_calories = portion2 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion2} {unicode2}')

SEA_PERCH_USER = pw_input("Enter how much grams sea perch you need", type=FLOAT, required=True)
portion3 = SEA_PERCH_USER * SEA_PERCH / 100
total_calories = portion3 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion3} {unicode3}')

RED_SWEET_PEPPER_USER = pw_input("Enter how much grams red sweet pepper you need", type=FLOAT, required=True)
portion4 = RED_SWEET_PEPPER_USER * RED_SWEET_PEPPER / 100
total_calories = portion4 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion4} {unicode4}')

PARSLEY_USER = pw_input("Enter how much grams parsley you need", type=FLOAT, required=True)
portion5 = PARSLEY_USER * PARSLEY / 100
total_calories = portion5 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion5} {unicode5}')

BANANAS_USER = pw_input("Enter how much grams bananas you need", type=FLOAT, required=True)
portion6 = BANANAS_USER * BANANAS / 100
total_calories = portion6 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion6} {unicode6}')

WAFFLES_USER = pw_input("Enter how much grams waffles you need", type=FLOAT, required=True)
portion7 = WAFFLES_USER * WAFFLES / 100
total_calories = portion7 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion7} {unicode7}')

WHEAT_BREAD_USER = pw_input("Enter how much grams wheat bread you need", type=FLOAT, required=True)
portion8 = WHEAT_BREAD_USER * WHEAT_BREAD / 100
total_calories = portion8 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion8} {unicode8}')

PISTACHOS_USER = pw_input("Enter how much grams pistachos you need", type=FLOAT, required=True)
portion9 = PISTACHOS_USER * PISTACHOS / 100
total_calories = portion9 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion9} {unicode9}')

KEFIR_TWO_AND_HALF_INTEREST_USER = pw_input("Enter how much grams kefir you need", type=FLOAT, required=True)
portion10 = KEFIR_TWO_AND_HALF_INTEREST_USER * KEFIR_TWO_AND_HALF_INTEREST / 100
total_calories = portion10 + total_calories
put_success(f'Full calorie content of the order: {total_calories}, product calorie content: {portion10} {unicode10}')

if total_calories < 1000:
    put_warning("You will be hungry, you need to eat more!")
elif total_calories < 1500:
    put_success("This is the perfect dinner option!")
    toast(f'Bon appetit! {unicode12}')
else:
    put_warning("Do you want to be obese? You need to eat less food!")

price = total_calories * price_one_calorie
cost = Decimal(str(price)).quantize(Decimal('0.01'))
put_success(f'The total cost of the order is {cost} hryvnia {unicode11}')
