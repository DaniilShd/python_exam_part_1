import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(message)s')

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

print(read_file('synonyms.txt'))