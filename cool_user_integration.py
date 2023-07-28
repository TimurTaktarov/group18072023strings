from pywebio.input import input as pw_input
from pywebio.output import put_success
user_name = pw_input('Enter your name: ').title()
print(user_name)