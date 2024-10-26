import logging

#Настройка логирования
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(message)s')

#Чтение файла используя try, вывод данных файла в виде словаря (кдлюч - слово, значения - синонимы)
def read_file(filename):
    synonyms_dict = dict()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                line = line.replace(" ", '').replace("\n", '').split('-')
                key = line[0]
                value = line[1].split(',')
                synonyms_dict[key] = value
                line = file.readline()
        logging.info("словарь сформирован")
        return synonyms_dict
    except FileNotFoundError:
        logging.error("file not found")
    except Exception as err:
        logging.error(f'{err}')

#Нахождение синонимов по ключу в словаре
def  get_synonyms(word, filename):
    synonyms_dict = read_file(filename)
    logging.info(f'Введено слово - {word}')
    if word in synonyms_dict.keys():
        result = f'{word} - '
        for i in range(0, len(synonyms_dict[word])):
            result += f'{i+1}). {synonyms_dict[word][i]}, '
        result = result[:-2] + '.'
        print(result)
    else:
        answer = "Указанного слова нет в словаре"
        print(answer)
        logging.info(answer)

#Ввод целевого слова и подбор синонимов
def get_word():
    word = input("Введите слово").lower()
    get_synonyms(word, 'synonyms.txt')

#Запуск скрипта
get_word()
