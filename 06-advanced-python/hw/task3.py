"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""


class ShiftDescriptor:
    def __init__(self, key):
        self.key = key
        self.dicL = {chr(x): x-97 for x in range(97, 123)}  # little letters
        self.dicB = {chr(x): x-65 for x in range(65, 91)}  # big letters

    def __get__(self, instance, owner):
        new_str = ''
        for i in self.value:
            if i not in self.dicL:
                if i not in self.dicB:
                    new_str += i
                    continue
                else:
                    ch = self.dicB[i] + self.key
                    if ch > 25:
                        ch = ch - 26
                    new_str += self._get_key(self.dicB, ch)
            else:
                ch = self.dicL[i] + self.key
                if ch > 25:
                    ch = ch - 26
                new_str += self._get_key(self.dicL, ch)
        return new_str

    def __set__(self, instance, value):
        self.value = value

    @staticmethod
    def _get_key(dic, val):
        for i in dic.items():
            if val in i:
                return i[0]


class CeasarSipher:
    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)
    other = ShiftDescriptor(15)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'
a.other = 'ZeNA'

assert a.message == 'efg'
assert a.another_message == 'olssv'
assert a.other == 'OtCP'
