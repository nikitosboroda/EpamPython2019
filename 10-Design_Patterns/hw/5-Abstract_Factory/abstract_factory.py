"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""
import yaml


class AbstractFactory:
    def __init__(self, menu):
        self.menu = menu

    def first_courses(self, day):
        pass

    def second_courses(self, day):
        pass

    def drinks(self, day):
        pass


class MenuVegan(AbstractFactory):
    def first_courses(self, day):
        return self.menu[day]['first_courses']['vegan']

    def second_courses(self, day):
        return self.menu[day]['second_courses']['vegan']

    def drinks(self, day):
        return self.menu[day]['drinks']['vegan']


class MenuChild(AbstractFactory):
    def first_courses(self, day):
        return self.menu[day]['first_courses']['child']

    def second_courses(self, day):
        return self.menu[day]['second_courses']['child']

    def drinks(self, day):
        return self.menu[day]['drinks']['child']


class MenuChina(AbstractFactory):
    def first_courses(self, day):
        return self.menu[day]['first_courses']['china']

    def second_courses(self, day):
        return self.menu[day]['second_courses']['china']

    def drinks(self, day):
        return self.menu[day]['drinks']['china']


with open('menu.yml', encoding="utf8") as f:
    menu = yaml.safe_load(f)
vegan = MenuVegan(menu)
child = MenuChild(menu)
china = MenuChina(menu)
print('Saturdays menu for China:')
print(china.first_courses('Saturday'))
print(china.second_courses('Saturday'))
print(china.drinks('Saturday'))
