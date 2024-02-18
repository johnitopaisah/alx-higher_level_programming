#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    l_digit = number % 10
else:
    l_digit = ((number * -1) % 10) * -1

message = "Last digit of {} is {}".format(number, l_digit)

if l_digit == 0:
    print(message)
elif l_digit > 5:
    print(message, "and is greater than 5")
else:
    print(message, "and is less than 6 and not 0")
