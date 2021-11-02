from helper import Helper, Point


class Task11:

    __task_number = 11

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить координаты вершины параболы y=ax2+bx+c (a!=0). Коэффициенты a,b,c заданы')

        data_list = list()
        helper.set_value_description_start_letter(data_list, 3, 'Введите коэфициент', 'a', True)

        a = data_list[0]
        b = data_list[1]
        c = data_list[2]

        point = self.__get_coord(a, b, c)

        print(f'Координаты вершины параболы = ({point.x}, {point.y})')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_coord(self, a: float, b: float, c: float) -> Point:
        try:
            x = round(-b / (2 * a), 2)
            y = round(a * pow(x, 2) + b * x + c, 2)
            return Point(x, y)
        except:
            print('Недопустимые значения входных данных (a = 0), начните с начала')
            self.task_ended_callback(self.task_number)
