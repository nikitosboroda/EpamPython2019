# -*- coding: utf-8 -*-
import functools
import time


def make_cache(sec=10):
    func_result = {}

    def decorator(func):
        @functools.wraps(func)
        def inner(*args):
            strt = time.time()
            key = args
            if key in func_result:
                if strt - func_result[key][1] > sec:
                    func_result.pop(key)
            else:
                result = func(*args)
                func_result[key] = (result, time.time())
            return result
        return inner
    return decorator


@make_cache(10)
def slow_function(a, b, c, *args):
    """Unknown function"""
    print(slow_function.__doc__)
    print(slow_function.__name__)
    print(args)
    return "Прямоугольный треугольник" if a ** 2 + b ** 2 == c ** 2 else "Не прямоугольный"


if __name__ == '__main__':
    slow_function(4, 5, 16, 33, 3423)
    print(dir(make_cache))
    slow_function(3, 4, 5)
