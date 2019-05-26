# -*- coding: utf-8 -*-
def atom(val=None):
    def get_value():
        return val

    def set_value():
        nonlocal val
        val = input()
        return val

    def process_value(*args):
        x = []
        for i in args:
            x.append(i())
        return x

    def delete_value(direct):
        while direct:
            del direct[0]

    direct = dir()

    return get_value(), set_value(), process_value(set_value, get_value), delete_value(direct)


print(atom(5))