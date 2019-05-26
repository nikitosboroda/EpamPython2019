# -*- coding: utf-8 -*-
def letters_range(stoop, strt=None, steep=1, **kwargs):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    print(kwargs)
    print(stoop, strt, steep)
    if not strt and steep < 0:
        return [letters[x] for x in range(letters.index(strt), letters.index(stoop), steep)]
    elif strt:
        return [letters[x] for x in range(letters.index(stoop), letters.index(strt), steep)]
    return [letters[x] for x in range(letters.index('a'), letters.index(stoop))]


print(letters_range('h', **{'y': 1, 'z': 2}))
print(letters_range('f', 'z'))
print(letters_range('h', 'a', -3))
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
