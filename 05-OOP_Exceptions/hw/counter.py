"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
from functools import wraps

def instances_counter(cls):
    setattr(cls, 'count_obj', 0)
    original = cls.__init__

    def increment_count_obj(*args, **kwargs):
        cls.count_obj += 1
        original(*args, **kwargs)

    def get_created_instances(*args, **kwargs):
        return cls.count_obj

    def reset_instances_counter(*args, **kwargs):
        result, cls.count_obj = cls.count_obj, 0
        return result

    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter
    cls.__init__ = increment_count_obj

    return cls


@instances_counter
class User:
    def __init__(self, name):
        self.name = name


@instances_counter
class Polzovatel:
    pass


if __name__ == '__main__':
    print(User.get_created_instances())  # 0
    user, _, _ = User(333), User(333), User(555)
    print(user.name)
    polzovatel, _ = Polzovatel(), Polzovatel()
    print(polzovatel.get_created_instances())  # 2
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.reset_instances_counter())  # 0
    print(polzovatel.get_created_instances())  # 2
