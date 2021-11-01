class Task1:

    __task_number = 1

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности')
        cube_edge = self.__set_value()
        print(f'Объем куба = {self.__get_cube_volume(cube_edge)}')
        print(f'Площадь боковой поверхности = {self.__get_lateral_surface_area(cube_edge)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_cube_volume(cube_edge):
        return round((cube_edge * cube_edge * cube_edge), 2)

    @staticmethod
    def __get_lateral_surface_area(cube_edge):
        return round((4 * pow(cube_edge, 2)), 2)

    def __set_value(self) -> float:
        while True:
            value = input('Введите длину ребра куба: ')
            if self.__is_valid(value):
                return float(value)
            else:
                continue

    @staticmethod
    def __is_valid(value) -> bool:
        try:
            value = float(value)
            if value > 0.0:
                return True
            else:
                print('Неверное значение, повторите')
                return False
        except:
            print('Неверное значение, повторите')
            return False
