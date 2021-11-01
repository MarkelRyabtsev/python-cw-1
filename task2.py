class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Три сопротивления R1, R2, R3 соединены параллельно. Найти сопротивление соединения')
        resist_list = list()
        self.__set_value(resist_list, 3)

        print(f'Сопротивление соединения = {self.__get_total_resist(resist_list)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_total_resist(resist_list) -> float:
        resist_sum = 0
        for resist in resist_list:
            resist_sum += 1 / resist

        return round((1 / resist_sum), 3)

    def __set_value(self, data_list: list, count: int):
        counter = 1
        while counter != count + 1:
            while True:
                value = input(f'R{counter} = ')
                if self.__is_valid(value):
                    counter += 1
                    data_list.append(float(value))
                    break
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
