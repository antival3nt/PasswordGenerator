import secrets as sec
import string

def passGen():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    pwd_length = input("Input password length: ")
    the_holy_grail = letters + digits + special_chars

    pwd = ''
    for i in range(int(pwd_length)):
        pwd += ''.join(sec.choice(the_holy_grail))

    print(pwd)