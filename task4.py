import math
from helper import Helper


class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Известна длина окружности. Найти площадь круга, ограниченного этой окружностью')
        circle_length = helper.set_value_simple('Введите длину окружности:')
        print(f'Площадь круга = {self.__get_circle_area(circle_length)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_circle_area(circle_length):
        return round(((circle_length * circle_length) / (4 * math.pi)), 2)
