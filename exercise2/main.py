import logging
import sys

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


def open_file(name):
    result_dict = {}
    try:
        with open(name, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                line = line.replace('\n', '')
                list_student = line.split(',')
                result_dict[list_student[0]] = []
                for i in range(1, len(list_student)):
                    result_dict[list_student[0]].append(list_student[i])
                line = file.readline()
        return result_dict
    except FileNotFoundError:
        my_log.error(f"{name} not found")
    except IOError:
        my_log.error(f"{name} IOError")

def student_of_score(students, score):
    result = []
    for name_student, value in students.items():
        total_score = 0
        count = 0
        for i in value:
            total_score += int(i)
            count += 1
        average_score = total_score/count
        if average_score > score:
            result.append(name_student)
    return result


def top_students(score, filename):
    students = student_of_score(open_file(filename), score)
    try:
        with open('top_students.txt', 'w', encoding='utf-8') as file:
            file.writelines(students)
    except IOError:
        my_log.error(f"file IOError")
    finally:
        my_log.info(f"file close")

top_students(4,'students.txt' )