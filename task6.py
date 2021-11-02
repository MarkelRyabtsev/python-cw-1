import math
from helper import Helper


class Task6:

    __task_number = 6

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить высоту треугольника, опущенную на сторону а, по известным значениям длин его сторон a, b, c')

        data_list = list()
        helper.set_value_description_start_letter(data_list, 3, 'Длина стороны', 'a')

        a = data_list[0]
        b = data_list[1]
        c = data_list[2]

        print(f'Высота треугольника на сторону а = {self.__get_height(a, b, c)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_height(a: float, b: float, c: float) -> float:
        p = 0.5 * (a + b + c)
        return round(
            (2 * ((math.sqrt(p * (p - a) * (p - b) * (p - c))) / a)),
            2
        )
