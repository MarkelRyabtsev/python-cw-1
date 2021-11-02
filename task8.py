import math
from helper import Helper


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить объем цилиндра с радиусом основания r и высотой h')
        r = helper.set_value_simple('Радиус основания')
        h = helper.set_value_simple('Высота')

        print(f'Объем цилиндра = {self.__get_volume(r, h)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_volume(r: float, h: float) -> float:
        return round(
            (math.pi * pow(r, 2) * h),
            2
        )
