#!/usr/bin/python3
for num in range(15):
    if num == 14:
        print("{:02d}".format(num))
    else:
        print("{:02d}".format(num), end=", ")
