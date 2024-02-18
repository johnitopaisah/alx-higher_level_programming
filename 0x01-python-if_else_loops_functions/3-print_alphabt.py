#!/usr/bin/python3
for charact in range(97, 123):
    if charact == 101:
        continue
    elif charact == 113:
        continue
    print("{:c}".format(charact), end='')
