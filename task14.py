import math
from helper import Helper


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('По данным сторонам прямоугольника вычислить его периметр, площадь и длину диагонали')

        a = helper.set_value_simple('Сторона a')
        b = helper.set_value_simple('Сторона b')

        print(f'Периметр = {self.__get_perimeter(a, b)}')
        print(f'Площадь = {self.__get_area(a, b)}')
        print(f'Длина диагонали = {self.__get_diagonal_length(a, b)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_perimeter(a: float, b: float) -> float:
        return round(
            (2 * (a + b)),
            2
        )

    @staticmethod
    def __get_area(a: float, b: float) -> float:
        return round(
            (a * b),
            2
        )

    @staticmethod
    def __get_diagonal_length(a: float, b: float) -> float:
        return round(
            (math.sqrt(pow(a, 2) + pow(b, 2))),
            2
        )
