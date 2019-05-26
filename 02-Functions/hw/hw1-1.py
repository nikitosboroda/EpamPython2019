# -*- coding: utf-8 -*-
def letters_range(*args, **kwargs):
	letters = [chr(x) for x in range(97,123)]
	if kwargs:
		for i in kwargs:
			letters[letters.index(i)] = kwargs[i]
			
	if len(args) == 1:
		stoop = letters.index(args[0])
		return [x for x in letters[:stoop:1]]
	elif len(args) == 2:
		strt = letters.index(args[0])
		stoop = letters.index(args[1])
		return [x for x in letters[strt:stoop:1]]
	elif len(args) == 3:
		strt = letters.index(args[0])
		stoop = letters.index(args[1])
		steep = args[2]
		return [x for x in letters[strt:stoop:steep]]

print(letters_range('a', 'z', 2))
print(letters_range('z', 'f', -2))
print(letters_range('z', **{'y': 10, 'a':6}))
print(letters_range('g', 'z'))