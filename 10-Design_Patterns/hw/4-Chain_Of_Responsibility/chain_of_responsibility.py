"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""


class Fridge:
    def __init__(self, eggs, flour, milk, sugar, oil, butter):
        self.eggs = eggs
        self.flour = flour
        self.milk = milk
        self.sugar = sugar
        self.oil = oil
        self.butter = butter


class AbstractHandler:
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler

    def handle(self):
        if self._next_handler:
            return self._next_handler.handle(req)
        return 'Oops'


class CheckEggs(AbstractHandler):
    def handle(self, fridge):
        print('CHECK EGGS')
        if fridge.eggs < 2:
            print(f"Need to buy {2-fridge.eggs} egg(s)")
        else:
            print('OK')
        self._next_handler.handle(fridge)


class CheckFlour(AbstractHandler):
    def handle(self, fridge):
        print('CHECK FLOUR')
        if fridge.flour < 300:
            print(f"Need to buy {300-fridge.flour} gramm of flour")
        else:
            print('OK')
        self._next_handler.handle(fridge)


class CheckMilk(AbstractHandler):
    def handle(self, fridge):
        print('CHECK MILK')
        if fridge.milk < 0.5:
            print(f"Need to buy {0.5-fridge.milk} liter(s) of milk")
        else:
            print('OK')
        self._next_handler.handle(fridge)


class CheckSugar(AbstractHandler):
    def handle(self, fridge):
        print('CHECK SUGAR')
        if fridge.sugar < 100:
            print(f"Need to buy {100-fridge.sugar} gramm of sugar")
        else:
            print('OK')
        self._next_handler.handle(fridge)


class CheckOil(AbstractHandler):
    def handle(self, fridge):
        print('CHECK OIL')
        if fridge.eggs < 10:
            print(f"Need to buy {10-fridge.oil} ml of oil")
        else:
            print('OK')
        self._next_handler.handle(fridge)


class CheckButter(AbstractHandler):
    def handle(self, fridge):
        print('CHECK BUTTER')
        if fridge.butter < 120:
            print(f"Need to buy {120-fridge.butter} gramm of butter")
        else:
            print('OK')


if __name__ == '__main__':
    fridge = Fridge(2, 100, 0.5, 100, 10, 120)
    checkEggs = CheckEggs()
    checkFlour = CheckFlour()
    checkMilk = CheckMilk()
    checkSugar = CheckSugar()
    checkOil = CheckOil()
    checkButter = CheckButter()

    checkEggs.set_next(checkFlour)
    checkFlour.set_next(checkMilk)
    checkMilk.set_next(checkSugar)
    checkSugar.set_next(checkOil)
    checkOil.set_next(checkButter)

    checkEggs.handle(fridge)
