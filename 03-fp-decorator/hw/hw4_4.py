# -*- coding: utf-8 -*-
import functools
import time


def make_cache(sec=10):
    func_result = {}

    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            strt = time.time()
            key = (args, kwargs) if args and kwargs else (args,)
            if key in func_result:
                if strt - func_result[key][1] > sec:
                    func_result.pop(key)
            else:
                result = func(*args, **kwargs)
                func_result[key] = (result, time.time())
        return inner
    return decorator


@make_cache(10)
def slow_function(a, b, c):
    """Unknown function"""
    print(slow_function.__doc__)
    print(slow_function.__name__)
    return "Прямоугольный треугольник" if a ** 2 + b ** 2 == c ** 2 else "Не прямоугольный"


if __name__ == '__main__':
    #print("RES:", func_result)
    slow_function(4, 5, 16)
    slow_function(3, 4, 5)
    #print("RES:", func_result)
