import math


class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Известна длина окружности. Найти площадь круга, ограниченного этой окружностью')
        circle_length = self.__set_value()
        print(f'Площадь круга = {self.__get_circle_area(circle_length)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_circle_area(circle_length):
        return round(((circle_length * circle_length) / (4 * math.pi)), 2)

    def __set_value(self) -> float:
        while True:
            value = input('Введите длину окружности: ')
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
