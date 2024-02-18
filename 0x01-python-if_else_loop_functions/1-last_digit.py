#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10
if l_digit == 0:
    print("Last digit of {} is {}".format(number, l_digit))
else:
    if number < 0:
        number = -(number)
        l_digit = number % 10
        print("Last digit of -{} is -{} and is less than 6 and not 0".format(number, l_digit))
    else:
        if l_digit > 5:
            print("Last digit of {} is {} and is greater than 5".format(number, l_digit))
        else:
            print("Last digit of -{} is -{} and is less than 6 and not 0".format(number, l_digit))
