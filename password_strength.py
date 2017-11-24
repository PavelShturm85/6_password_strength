
import string
from getpass import getpass


def load_data(enter_file):
    with open(enter_file, 'r') as password_file:
        return password_file.read()


def get_password_strength(psw, black_list):
    password_strength = 0
    uniqueness_rate = 0.8
    if black_list.find(psw) != -1:
        return password_strength
    else:
        if len(set(psw)) >= len(psw)*uniqueness_rate and len(psw) >= 10:
            password_strength += 6

        upper = set(string.ascii_uppercase)
        lower = set(string.ascii_lowercase)
        digits = set(string.digits)
        punctuation = set(string.punctuation)
        letters = set(psw)

        for pattern in (upper, lower, digits, punctuation):
            if pattern & letters:
                password_strength += 1
    return password_strength


if __name__ == '__main__':

    input_password = getpass()
    password_black_list = load_data('passwords.txt')
    print("Password strength is -{}- from 10.".format(
        get_password_strength(input_password, password_black_list)))
