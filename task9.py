from helper import Helper


class Task9:

    __task_number = 9

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить расстояние, пройденное физическим телом за время t, если тело движется '
              '\nс постоянным ускорением а и имеет в начальный момент времени скорость V0')
        t = helper.set_value_simple('Время (сек)')
        a = helper.set_value_simple('Ускорение (м/сек^2)')
        v0 = helper.set_value_simple('Скорость в начальный момент (м/сек)')

        print(f'Пройденное расстояние = {self.__get_distance(t, a, v0)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_distance(t: float, a: float, v0: float) -> float:
        return round(
            ((v0 * t) + ((a * pow(t, 2)) / 2)),
            2
        )
