import math
from helper import Helper, Point


class Task5:

    __task_number = 5

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Треугольник задан координатами своих вершин. Найти: '
              '• периметр треугольника' 
              '• площадь треугольника')
        coordinate_list = list()

        print(f'Введите координаты точки A:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_a = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print(f'Введите координаты точки B:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_b = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print(f'Введите координаты точки C:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_c = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()

        print('----------------------------------------------------------')
        print(f'A({point_a.x}, {point_a.y})')
        print(f'B({point_b.x}, {point_b.y})')
        print(f'C({point_c.x}, {point_c.y})')

        perimeter = self.__get_perimeter(point_a, point_b, point_c)

        print(f'Периметр треугольника = {perimeter}')
        print(f'Площадь треугольника = {self.__get_area(point_a, point_b, point_c, perimeter)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_area(self, a: Point, b: Point, c: Point, perimeter) -> float:
        ab = self.__get_vector_length(a, b)
        bc = self.__get_vector_length(b, c)
        ac = self.__get_vector_length(a, c)
        half_perimeter = perimeter / 2
        return round(
            (math.sqrt(half_perimeter * (half_perimeter - ab) * (half_perimeter * bc) * (half_perimeter * ac))),
            2
        )

    def __get_perimeter(self, a: Point, b: Point, c: Point) -> float:
        ab = self.__get_vector_length(a, b)
        bc = self.__get_vector_length(b, c)
        ac = self.__get_vector_length(a, c)
        return round((abs(ab) + abs(bc) + abs(ac)), 2)

    @staticmethod
    def __get_vector_length(first: Point, second: Point) -> float:
        return round(math.sqrt(pow((first.x - second.x), 2) + pow((first.y - second.y), 2)), 2)
