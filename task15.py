import math
from helper import Helper, Point


class Task15:

    __task_number = 15

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить расстояние на плоскости между двумя точками с заданными координатами M1(x1,y1) и M2(x2,y2)')
        coordinate_list = list()

        print(f'Введите координаты точки M1:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_m1 = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print(f'Введите координаты точки M2:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_m2 = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print('----------------------------------------------------------')
        print(f'M1({point_m1.x}, {point_m1.y})')
        print(f'M2({point_m2.x}, {point_m2.y})')

        print(f'Расстояние между точками = {self.__get_distance(point_m1, point_m2)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_distance(first: Point, second: Point) -> float:
        return round(math.sqrt(pow((second.x - first.x), 2) + pow((second.y - first.y), 2)), 2)
