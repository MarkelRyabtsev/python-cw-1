import math
from helper import Helper


class Task7:

    __task_number = 7

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить значение функции y = ae^(−ax) * sin(ωx) при x = (π / 2 − φ) / ω')

        a = helper.set_value_simple('a')
        omega = helper.set_value_simple('ω', 0, True)
        phi = helper.set_value_simple('φ')

        x = self.__get_x(a, omega, phi)
        y = self.__get_y(a, omega, x)

        print(f'y = {y}, x = {x}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_x(a: float, omega: float, phi: float) -> float:
        return round((((math.pi / 2) * phi) / omega), 2)

    @staticmethod
    def __get_y(a: float, omega: float, x: float) -> float:
        return round((a * math.exp(-a * x) * math.sin(omega * x)), 4)
