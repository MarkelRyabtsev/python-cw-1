import math
from helper import Helper, Point


class Task16:

    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить координаты точки, делящей отрезок в соотношении')
        coordinate_list = list()

        print(f'Введите координаты точки A:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_a = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print(f'Введите координаты точки B:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_b = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print(f'Введите соотношение деления отрезка:')
        n1 = helper.set_value_simple('n1')
        n2 = helper.set_value_simple('n2')

        print('----------------------------------------------------------')
        print(f'A({point_a.x}, {point_a.y})')
        print(f'B({point_b.x}, {point_b.y})')
        print(f'Соотношение деления {n1} : {n2}')

        point = self.__get_coord(point_a, point_b, n1, n2)

        print(f'Координаты делящей точки = ({point.x}, {point.y})')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_coord(first: Point, second: Point, n1: float, n2: float) -> Point:
        n = n1 / n2
        x = round((first.x + (n * second.x)) / (1 + n), 2)
        y = round((first.y + (n * second.y)) / (1 + n), 2)
        return Point(x, y)
