from helper import Helper


class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Три сопротивления R1, R2, R3 соединены параллельно. Найти сопротивление соединения')
        resist_list = list()
        helper.set_value_description_counter(resist_list, 3, 'R')

        print(f'Сопротивление соединения = {self.__get_total_resist(resist_list)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_total_resist(resist_list) -> float:
        resist_sum = 0
        for resist in resist_list:
            resist_sum += 1 / resist

        return round((1 / resist_sum), 3)
