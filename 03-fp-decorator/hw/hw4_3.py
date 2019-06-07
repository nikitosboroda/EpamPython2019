# -*- coding: utf-8 -*-


def collatz_steps(n, count=0):
    if n != 1:
        n = (lambda x: x//2 if x%2==0 else x*3+1)(n)
        count += 1
    else:
        return count
    return collatz_steps(n, count)


print(collatz_steps(12))
print(collatz_steps(16))
print(collatz_steps(1000000))
