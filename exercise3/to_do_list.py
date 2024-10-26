import logging
import sys

#Настройка логирования
FORMATTER_STRING = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "app.log"

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger

my_log = get_logger("my_logger")

#Создается список задач и файл для записи
def create_task_list():
    tasks_list = []
    try:
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            file.close()
    except Exception as err:
        my_log.error(err)
    return tasks_list

#Функция для вставки задачи в список (с обновлением файла)
def insert_task(new_task, tasks_list):
    try:
        with open('tasks.txt', 'a', encoding='utf-8') as file:
            file.writelines(new_task)
    except FileNotFoundError as err:
        my_log.error(err)
    except Exception as err:
        my_log.error(err)
    tasks_list.append(new_task)

#Функция для удаления задачи из списка (с обновлением файла)
def delete_task(number_task_to_delete, tasks_list):
    tasks_list.pop(number_task_to_delete-1)
    try:
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            file.writelines(tasks_list)
    except FileNotFoundError as err:
        my_log.error(err)
    except Exception as err:
        my_log.error(err)
    return 0

def get_number_task_to_delete(tasks_list):
    number = int(input("Введите номер задачи для удаления из списка"))
    if number in range(1, len(tasks_list)+1):
        return number
    else:
        print("Вы ввели неверное значение")
        return 0

#Функция с бесконечным циклом для управления списка задач
def to_do_list():
    tasks_list = create_task_list()
    while True:
        list_answer = ['1', '2', '3']
        answer = input("Введите одну из команд:\n1)добавить запись\n2)удалить запись\n3)отображение задач")
        if answer not in list_answer:
            print("Вы ввели неверное значение")
        if answer == '1':
            task = input("Введите задачу")
            if task != '':
                insert_task(task, tasks_list)
            else:
                print("Вы ввели пустую строку, повторите попытку")
        if answer == '2':
            number_task_to_delete = get_number_task_to_delete(tasks_list)
            if number_task_to_delete == 0:
                continue
            if delete_task(number_task_to_delete, tasks_list) == 0:
                print("Задача успешно удалена")
        if answer == '3':
            print("Список дел:")
            for number in range(0, len(tasks_list)):
                print(f"{number+1}) {tasks_list[number]}")

#Стартовая функция
to_do_list()