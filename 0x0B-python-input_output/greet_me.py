#!/usr/bin/python3
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} == {}".format(key, value))

greet_me(name="yasoob")