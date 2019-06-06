# -*- coding: utf-8 -*-
from inspect import getcallargs
from inspect import getsource


def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_func(*args, **kwargs):
        nonlocal fixated_args, fixated_kwargs
        if agrs or kwargs:
            fixated_args += args
            fixated_kwargs = fixated_kwargs.update(kwargs)
        #func(fixated_args, fixated_kwargs)

    new_func.__name__ = f'func_{new_func.__name__}'
    # print(new_func.__name__)
    mass = []
    str = ''
    doc = 'None'
    if fixated_args:
        for i in args:
            mass.append(i)
        doc = getcallargs(modified_func, mass, fixated_kwargs)
    new_func.__doc__ = f'A func implementation of {func.__name__}\n' \
                       f'with pre-applied arguments being:\n' \
                       f'{doc}\n' \
                       f'source_code:\n' \
                       f'{getsource(func)}'
    print(new_func.__doc__)


def func():
    return "ERROR"


modified_func(func)