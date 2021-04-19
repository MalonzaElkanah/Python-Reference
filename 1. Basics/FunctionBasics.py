from random import randint


def numbertoguess():
    return randint(1, 20)


def guess():
    return int(input())


def checknumber(number, input_num):
    if number > input_num:
        print("The Number is too low")
        return False
    elif number < input_num:
        print("The Number is too high")
        return False
    else:
        print("Correct Number")
        return True


print("Guess a Number between 1 and 20: ")
num = numbertoguess()
for i in range(1, 7):
    num2 = guess()
    if checknumber(num, num2):
        print("Congratulations!")
        break
