import math
from helper import Helper


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить площадь поверхности и объем усеченного конуса')

        r_big = helper.set_value_simple('Радиус нижнего основания')
        r_small = helper.set_value_simple('Радиус верхнего основания', r_big, False)
        length = helper.set_value_simple('Длина образующей')
        height = helper.set_value_simple('Высота')

        print(f'Площадь поверхности = {self.__get_area(r_big, r_small, length)}')
        print(f'Объем = {self.__get_volume(r_big, r_small, height)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_area(r_big: float, r_small: float, length: float) -> float:
        return round(
            ((math.pi * (r_big + r_small) * length) + (math.pi * pow(r_big, 2)) + (math.pi * r_small)),
            2
        )

    @staticmethod
    def __get_volume(r_big: float, r_small: float, height: float) -> float:
        return round(
            ((1 / 3) * math.pi * (pow(r_big, 2) + pow(r_small, 2) + r_big * r_small) * height),
            2
        )
