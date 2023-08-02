from pywebio.input import input as pw_input
from pywebio.input import NUMBER,PASSWORD,TEXT,DATETIME,COLOR
from pywebio.output import put_success, put_warning, put_code,popup,toast

user_nickname = str(pw_input('Enter your nick')).title()
user_age = str(pw_input('Enter your age', type=NUMBER, required=True)).lstrip('-')

admin = 'Timur'
promouter = 'Oleg'

is_admin = user_nickname == admin
is_promouter = user_nickname == promouter
is_other_user = user_nickname != admin

if is_admin:
    put_success(f'Hello my master')
    put_success(f'I know, you are {user_age} years old xo-xo')

elif is_promouter:
    toast('NE GAZUY')

elif user_nickname:
    put_success(f'Hello, {user_nickname}')
    put_success(f'I know, you are {user_age} years old xo-xo')

else:
    put_warning('You have not entered nickname. Shame om you, pal')
