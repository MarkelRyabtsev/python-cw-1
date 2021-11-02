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

    def set_value_simple(self, description: str) -> float:
        while True:
            value = input(f'{description} : ')
            if self.__is_valid(value, True):
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

    def set_value_description_start_letter(self, data_list: list, count: int, description: str, start_letter: str):
        counter = 1
        value_name = start_letter
        while counter != count + 1:
            while True:
                value = input(f'{description} {value_name} = ')
                if self.__is_valid(value, True):
                    counter += 1
                    code = ord(value_name)
                    value_name = chr(code + 1)
                    data_list.append(float(value))
                    break
                else:
                    continue
