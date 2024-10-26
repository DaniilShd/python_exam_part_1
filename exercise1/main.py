import logging
import sys
import csv

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

#Чтение файла, возвращает список данных
def read_file(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data_text = file.readlines()
            result_list = []
            for item in data_text:
                item = item.replace('\n', '').split(',')
                result_list.append(item)
            my_log.info(f"{name} read")
            return result_list
    except FileNotFoundError:
        my_log.error(f"{name} not found")
    except Exception as err:
        my_log.error(f"{err}")
    finally:
        my_log.info(f"{name} end read file")

# Функция для подсчета общей суммы и суммы по строкам
def amount_of_item(data_list):
    total = 0
    result_amount_of_item = dict()
    for item in data_list:
        total += int(item[1]) * float(item[2])
        quantity = item[1]
        amount = int(item[1]) * float(item[2])
        price = item[2]
        result_amount_of_item[item[0]] = [quantity, amount, price]
    return total, result_amount_of_item

#Вывод результата и оформление в файл csv
def output_result(name, max_total):
    data = read_file(name)
    total, result_amount_of_item = amount_of_item(data)
    if total > max_total:
        print("Высокие продажи!")
    with open("result.csv", 'w', encoding='utf-8', newline='') as file:
        headers_list = ['name', 'quantity', 'price', 'amount']
        writer = csv.DictWriter(file, headers_list)
        writer.writeheader()
        for key, item in result_amount_of_item.items():
            row = [key, item[0], item[2], item[1]]
            dict_row = {}
            for key, value in zip(headers_list, row):
                dict_row[key] = value
            writer.writerow(dict_row)

output_result('data.txt', 50000)
