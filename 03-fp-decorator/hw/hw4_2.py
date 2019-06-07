# -*- coding: utf-8 -*-

def is_armstrong(number):
    return (lambda number: number == sum([int(i)**len(str(number)) for i in str(number)]))(number)


print(is_armstrong(9))
print(is_armstrong(10))
print(is_armstrong(153))
