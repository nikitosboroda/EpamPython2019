"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно
добавлять к кофе маршмеллоу,
взбитые сливки и сироп,
а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffe(Component):
    def get_cost(self):
        return 90


class Decorator(Component):
    """
    Базовый класс Декоратора следует тому же интерфейсу, что и другие
    компоненты. Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """
    _component = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        """
        Декоратор делегирует всю работу обёрнутому компоненту.
        """
        return self._component

    def get_cost(self):
        self._component.get_cost()


class Whip(Decorator):

    def get_cost(self):
        print("Добавлены взбитые сливки. Цена возросла на 20")
        return 20 + self.component.get_cost()


class Marshmallow(Decorator):

    def get_cost(self):
        print("Добавлен Marshmallow. Цена возросла на 50")
        return 50 + self.component.get_cost()


class Syrup(Decorator):

    def get_cost(self):
        print("Добавлен сироп. Цена возросла на 20")
        return 20 + self.component.get_cost()


if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))
