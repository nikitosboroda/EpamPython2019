# -*- coding: utf-8 -*-
counter_name = 1
b = 11
c = 12


def make_it_count(func, counter_name):
    def new_func(func):
        globals()[counter_name] += 1
        func()

    return new_func(func)


def other_func():
    return "smth"


# print(globals())
print(b)
make_it_count(other_func, 'b')
print(b)
