import math
from helper import Helper


class Task12:

    __task_number = 12

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить полную поверхность цилиндра Sполн=2*pi*R*(H+R)')

        r = helper.set_value_simple('Радиус основания')
        h = helper.set_value_simple('Высота')

        print(f'Площадь поверхности = {self.__get_area(r, h)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_area(r: float, h: float) -> float:
        return round(
            (2 * math.pi * r * (h + r)),
            2
        )
