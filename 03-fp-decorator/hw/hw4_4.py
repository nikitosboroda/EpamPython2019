# -*- coding: utf-8 -*-
import functools
import time
func_result = []


def make_cache(sec=10):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            func_result.append(result)
            time.sleep(sec)
            func_result.pop()
            return
        return inner
    return decorator


@make_cache(10)
def slow_function(a, b, c):
    """Unknown function"""
    print(slow_function.__doc__)
    print(slow_function.__name__)
    return "Прямоугольный треугольник" if a**2 + b**2 == c**2 else "Не прямоугольный"


if __name__ == '__main__':
    print("RES:", func_result)
    slow_function(4, 5, 16)
    slow_function(3, 4, 5)
    print("RES:", func_result)
