from helper import Helper, Point


class MaterialPoint:
    def __init__(self, weight, point: Point):
        self.weight = weight
        self.point = point


class Task10:

    __task_number = 10

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить координаты центра тяжести трех материальных точек с массами и координатами по формулам')

        coordinate_list = list()

        print(f'Введите координаты точки A:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_a = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()
        weight_a = helper.set_value_simple('Масса точки A:')

        print(f'Введите координаты точки B:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_b = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()
        weight_b = helper.set_value_simple('Масса точки B:')

        print(f'Введите координаты точки C:')
        helper.set_value_start_letter(coordinate_list, 2, 'X')
        point_c = Point(coordinate_list[0], coordinate_list[1])
        coordinate_list.clear()
        weight_c = helper.set_value_simple('Масса точки C:')

        a = MaterialPoint(weight_a, point_a)
        b = MaterialPoint(weight_b, point_b)
        c = MaterialPoint(weight_c, point_c)

        print('----------------------------------------------------------')
        print(f'A({a.point.x}, {a.point.y}) Масса = {a.weight}')
        print(f'B({b.point.x}, {b.point.y}) Масса = {b.weight}')
        print(f'C({c.point.x}, {c.point.y}) Масса = {b.weight}')

        weight_point = self.__get_distance(a, b, c)
        print(f'Координаты центра тяжести = ({weight_point.x}, {weight_point.y})')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_distance(a: MaterialPoint, b: MaterialPoint, c: MaterialPoint) -> Point:
        x0 = round(
            (a.weight * a.point.x + b.weight * b.point.x + c.weight * c.point.x) / (a.weight + b.weight + c.weight),
            2
        )
        y0 = round(
            (a.weight * a.point.y + b.weight * b.point.y + c.weight * c.point.y) / (a.weight + b.weight + c.weight),
            2
        )
        return Point(x0, y0)
