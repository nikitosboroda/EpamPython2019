"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как y словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго, проверку делаю автотестами и просмотром кода.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class DeadlineError(Exception):
    """Task overdue"""


class Teacher(Person):
    homework_done = defaultdict(dict)

    @staticmethod
    def create_homework(hw_text, days_for_task):
        return Homework(hw_text, days_for_task)

    @classmethod
    def check_homework(cls, hw_res_obj) -> bool:
        if len(hw_res_obj.solution) >= 5:
            if hw_res_obj.solution not in cls.homework_done:
                cls.homework_done[hw_res_obj.homework][hw_res_obj.solution] =\
                    hw_res_obj
                return True
        return False

    @classmethod
    def reset_results(cls, hw_obj=None) -> None:
        if hw_obj:
            if hw_obj in cls.homework_done:
                del cls.homework_done[hw_obj]
            else:
                print("HW doesn't exist")
        else:
            cls.homework_done.clear()


class Student(Person):
    def do_homework(self, hw_object, solution):
        if hw_object.is_active():
            return HomeworkResult(self, hw_object, solution)
        raise DeadlineError('You are late')


class Homework:
    def __init__(self, text: str, days: int):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = datetime.timedelta(days=days)

    def is_active(self) -> bool:
        return (datetime.datetime.now() - self.created) < self.deadline


class HomeworkResult:
    def __init__(self, author, task, solution: str):
        self.author = author
        self.created = datetime.datetime.now()
        self.solution = solution
        if isinstance(task, Homework):
            self.homework = task
        else:
            raise TypeError('You gave a not Homework object')

    def __str__(self):
        return f"Student {self.author} gave his " \
               f"solution: {self.solution} , at {self.created} o'clock"


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    # print('------', Teacher.homework_done)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
