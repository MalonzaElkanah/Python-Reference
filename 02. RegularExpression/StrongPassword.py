# regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit.

import re


def length(pw):
    pattern = re.compile(r'[\w]{8,}')
    try:
        pattern.search(pw).group()
        return True
    except AttributeError:
        return False


def mixed_case(pw):
    pattern = re.compile(r'([A-Z]+[a-z]+)|([a-z]+[A-Z]+)')
    try:
        pattern.search(pw).group()
        return True
    except AttributeError:
        return False


def digit(pw):
    pattern = re.compile(r'[0-9]+')
    try:
        pattern.search(pw).group()
        return True
    except AttributeError:
        return False


pass_q = str(input("ENTER A PASSWORD:"))
if not length(pass_q):
    print("Short Password: At least eight characters long")

elif not mixed_case(pass_q):
    print("No Mixed Case Password: contains both uppercase and lowercase characters")

elif not digit(pass_q):
    print("No Digit Password: contains has at least one digit")
else:
    print("Strong Password")
