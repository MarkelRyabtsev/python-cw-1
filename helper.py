class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Helper:

    @staticmethod
    def __is_valid(value, check_negative_value=False) -> bool:
        try:
            value = float(value)
            if check_negative_value:
                if value > 0.0:
                    return True
                else:
                    print('Неверное значение, повторите')
                    return False
            return True
        except:
            print('Неверное значение, повторите')
            return False

    def set_value_simple(self, description: str, limit: float = None, after_limit: bool = None) -> float:
        while True:
            value = input(f'{description} : ')
            if self.__is_valid(value, True):
                if limit is not None and after_limit is not None:
                    if float(value) > limit and after_limit:
                        return float(value)
                    elif float(value) > limit and not after_limit:
                        print(f'Значение должно быть меньше {limit}')
                        continue
                    elif float(value) < limit and after_limit:
                        print(f'Значение должно быть больше {limit}')
                        continue
                    elif float(value) < limit and not after_limit:
                        return float(value)
                    else:
                        print(f'Значения должны быть не равны')
                        continue
                return float(value)
            else:
                continue

    def set_value_description_counter(self, data_list: list, count: int, description: str):
        counter = 1
        while counter != count + 1:
            while True:
                value = input(f'{description}{counter} = ')
                if self.__is_valid(value, True):
                    counter += 1
                    data_list.append(float(value))
                    break
                else:
                    continue

    def set_value_start_letter(self, data_list: list, count: int, start_letter: str):
        counter = 1
        value_name = start_letter
        while counter != count + 1:
            while True:
                value = input(f'{value_name} = ')
                if self.__is_valid(value):
                    counter += 1
                    code = ord(value_name)
                    value_name = chr(code + 1)
                    data_list.append(float(value))
                    break
                else:
                    continue

    def set_value_description_start_letter(
            self,
            data_list: list,
            count: int,
            description: str,
            start_letter: str,
            use_negative_values=False
    ):
        counter = 1
        value_name = start_letter
        while counter != count + 1:
            while True:
                value = input(f'{description} {value_name} = ')
                if self.__is_valid(value, not use_negative_values):
                    counter += 1
                    code = ord(value_name)
                    value_name = chr(code + 1)
                    data_list.append(float(value))
                    break
                else:
                    continue
