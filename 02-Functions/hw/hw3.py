# -*- coding: utf-8 -*-


def make_it_count(func, var):
    def new_func(func):
        nonlocal var
        func()
        var += 1
        # return var

    return new_func(func)


def other_func():
    return "smth"


print(make_it_count(other_func, 3))
