
import re
import sys


def load_data(enter_file):
    with open(enter_file, 'r') as password_file:
        return password_file.read()


def get_password_strength(password, black_list):
    password_strength = 0
    if len(set(password)) >= len(password)*0.8 and len(password) >= 10:
        password_strength += 6
    for parameter in ('[a-z]', '[A-Z]', '[0-9]', '[$#@]'):
        if re.search(parameter, password):
            password_strength += 1
    if re.search(password, black_list):
        password_strength = 0
    return password_strength


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_password = sys.argv[1]
    else:
        input_password = input('Введите пароль: ')

    password_black_list = load_data('passwords.txt')
    print("Password strength is -{}- from 10.".format(
        get_password_strength(input_password, password_black_list)))
