import math
from helper import Helper


class Task3:

    __task_number = 3

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить значения функций y = (math.exp(-x1) + math.exp(-x2)) / 2 '
              'и z = ((a * math.sqrt(x1)) - (b * math.sqrt(x2))) / c')
        start_data = list()
        helper.set_value_start_letter(start_data, 3, 'a')

        a = start_data[0]
        b = start_data[1]
        c = start_data[2]

        x1 = self.__get_x1(start_data)
        x2 = self.__get_x2(start_data)
        print(f'x1 = ({b} + math.sqrt(abs(({b} * {b}) - (4 * {a} * {c})))) / (2 * {a}) = {x1}')
        print(f'x2 = ({b} - math.sqrt(abs(({b} * {b}) - (4 * {a} * {c})))) / (2 * {a}) = {x2}')

        y = self.__get_y(x1, x2)
        z = self.__get_z(start_data, x1, x2)
        print(f'y = (math.exp(-{x1}) + math.exp(-{x2})) / 2 = {y}')
        print(f'z = (({a} * math.sqrt({x1})) - ({b} * math.sqrt({x2}))) / c = {z}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_x1(start_data) -> float:
        a = start_data[0]
        b = start_data[1]
        c = start_data[2]
        return round((b + math.sqrt(abs((b * b) - (4 * a * c)))) / (2 * a), 2)

    @staticmethod
    def __get_x2(start_data) -> float:
        a = start_data[0]
        b = start_data[1]
        c = start_data[2]
        return round((b - math.sqrt(abs((b * b) - (4 * a * c)))) / (2 * a), 2)

    def __get_y(self, x1, x2) -> float:
        try:
            return round((math.exp(-x1) + math.exp(-x2)) / 2, 2)
        except ValueError:
            print('Недопустимые значения входных данных, начните с начала')
            self.task_ended_callback(self.task_number)

    def __get_z(self, start_data, x1, x2) -> float:
        a = start_data[0]
        b = start_data[1]
        c = start_data[2]
        try:
            return round(((a * math.sqrt(x1)) - (b * math.sqrt(x2))) / c, 2)
        except ValueError:
            print('Недопустимые значения входных данных, начните с начала')
            self.task_ended_callback(self.task_number)
