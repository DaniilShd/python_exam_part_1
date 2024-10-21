import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(levelname)s: %(message)s')

def read_file(filename):
    data_of_employees = dict()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                line = line.replace('\n', '').split(',')
                list_info = [int(line[1]), line[2], int(line[3])]
                data_of_employees[line[0]] = list_info
                line = file.readline()
            return data_of_employees
    except FileNotFoundError:
        logging.error(f"{filename} not found")
    except IOError:
        logging.error(f"{filename} IOError")
    except EOFError:
        logging.error(f"{filename} EOFError")
    except Exception as err:
        logging.error(f'Exception - {err}')


def average_salary(data_employees_salary):
    total_salary = 0
    for list_info in data_employees_salary.values():
        total_salary += list_info[2]
    try:
        average_sal = total_salary / len(data_employees_salary)
        logging.info(f'average salary - {average_sal}')
        return average_sal
    except ZeroDivisionError as err:
        logging.error(err)

def filter_employees(data_list_employees):
    aver_salary = average_salary(data_list_employees)
    list_of_high_earners = []
    for employee, salary in data_list_employees.items():
        if salary[2] > aver_salary:
            list_of_high_earners.append(employee)
    return list_of_high_earners

def write_to_high_earners(list_of_high_earners, data_dict_employees):
    try:
        with open('high_earners.txt', 'w', encoding='utf-8') as file:
            for employee in list_of_high_earners:
                str_to_write = f'{employee} - {data_dict_employees[employee][1]} - {data_dict_employees[employee][2]}\n'
                file.write(str_to_write)
    except Exception as err:
        logging.error(f"{err}")


def start():
    data_dict_employees = read_file('employees.txt')
    list_of_high_earners = filter_employees(data_dict_employees)
    write_to_high_earners(list_of_high_earners, data_dict_employees)

start()

