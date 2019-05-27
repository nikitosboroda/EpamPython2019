# -*- coding: utf-8 -*-
counter_name = 1

def make_it_count(func, var):
    def new_func(func):
        global counter_name
        func()
        counter_name += 1
		
    return new_func(func)

def other_func():
	return "smth"
	
	
print(make_it_count(other_func, counter_name))
