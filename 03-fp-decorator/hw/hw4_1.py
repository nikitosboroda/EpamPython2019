# -*- coding: utf-8 -*-
from functools import reduce


def problem9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product: abc.
    """
    return reduce(lambda x, y: x*y, [[a, b, 1000 - a - b] for a in range(1, 1001) for b in range(a, 1001)
           if a ** 2 + b ** 2 == (1000 - a - b) ** 2][0])

def problem6():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
    """
    return sum([x for x in range(1, 101)])**2 - sum([x**2 for x in range(1, 101)])


def problem40():
    """
    An irrational decimal fraction is created by concatenating the positive integers:
    0.123456789101112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.
    If Dn represents the Nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
     """
    mass = [int(''.join(str(c) for c in range(1000001))[10 ** k]) for k in range(7)]
    return reduce(lambda x, y: x * y, mass)



def problem48():
    """
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    return sum([x**x for x in range(1, 1001)]) % 10**10


print('Problem9:', problem9())
print('Problem6:', problem6())
print('Problem40:', problem40())
print('Problem48:', problem48())
