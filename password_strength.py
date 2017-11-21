
import re
import sys


def get_password_strength(password):
    password_strength = 0
    if re.search('[A-Z]', password):
        password_strength += 1
    if re.search('[a-z]', password):
        password_strength += 1
    if re.search('[0-9]', password):
        password_strength += 1
    if re.search('[$#@]', password):
        password_strength += 1
    if re.search('\s', password):
        password_strength += 1
    if len(set(password)) >= len(password)*0.8 and len(password) >= 10:
        password_strength += 5
    return password_strength


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_password = sys.argv[1]
    else:
        input_password = input('Введите пароль: ')
    print("Password strength is -{}- from 10.".format(
        get_password_strength(input_password)))
