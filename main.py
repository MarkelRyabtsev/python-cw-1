def show_main_menu():
    print('----------------------------------------------------------')
    number = int(input('Введите номер задачи : '))
    if 1 <= number <= 16:
        __go_to_task(number)
    else:
        print('Неверный номер, повторите')
        show_main_menu()


def __go_to_task(number: int):
    if number == 1:
        from task1 import Task1
        task = Task1(task_ended_callback)
        task.start_task()
    elif number == 2:
        from task2 import Task2
        task = Task2(task_ended_callback)
        task.start_task()
    elif number == 3:
        from task3 import Task3
        task = Task3(task_ended_callback)
        task.start_task()
    elif number == 4:
        from task4 import Task4
        task = Task4(task_ended_callback)
        task.start_task()
    elif number == 5:
        from task5 import Task5
        task = Task5(task_ended_callback)
        task.start_task()
    else:
        print('?')


def task_ended_callback(number: int):
    a = float(input('Назад к задачам(1), повторить задачу(2): '))
    if a == 1:
        show_main_menu()
    elif a == 2:
        __go_to_task(number)
    else:
        print('Неверный номер, повторите')
        task_ended_callback(number)


show_main_menu()
