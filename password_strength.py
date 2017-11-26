
import string
from getpass import getpass


def load_data(enter_file):
    with open(enter_file, 'r') as password_file:
        return password_file.read().splitlines()


def get_password_strength(password, black_list):
    password_strength = 0
    uniqueness_rate = 0.8
    if password in black_list:
        return password_strength
    else:
        if len(set(password)) >= len(password)*uniqueness_rate \
           and len(password) >= 10:
            password_strength += 6

        upper = set(string.ascii_uppercase)
        lower = set(string.ascii_lowercase)
        digits = set(string.digits)
        punctuation = set(string.punctuation)
        set_password = set(password)

        for pattern in (upper, lower, digits, punctuation):
            if pattern & set_password:
                password_strength += 1
        return password_strength


if __name__ == '__main__':

    input_password = getpass()
    forbidden_passwords = load_data('passwords.txt')
    print("Password strength is -{}- from 10.".format(
        get_password_strength(input_password, forbidden_passwords)))
