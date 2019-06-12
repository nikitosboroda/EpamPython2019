# -*- coding: utf-8 -*-
counter_name = 1

def make_it_count(func, counter_name):
    def new_func(func):
        global counter_name
        func()
        counter_name += 3
        # return counter_name

    return new_func(func)


def other_func():
    return "smth"


print(make_it_count(other_func, counter_name))
print(counter_name)
