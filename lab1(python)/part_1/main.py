import hashlib
import string
import random
from encoding import Encoding
from hash_functions import HashFunctions
from parser import get_parser


size_of_string_begin = 100  # Минимальный размер строки
size_of_string_end = 150  # максимальный размер строк


parser = get_parser()
arguments = parser.parse_args()
file_path = arguments.file  # текстовый файл с паролями
encoding = arguments.encoding  # кодировка
hash_functions = arguments.functions  # хеш функция
number_of_str = arguments.number  # количество хеш значений в выходном файле
file_path_out = arguments.output  # текстовый файл для записи информации
hash_obj = hashlib.new(hash_functions)


def create_hash(str):
    hash_obj.update(str.encode(encoding=encoding))
    return hash_obj.hexdigest()


def generate_random_str(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def create_random_str_hash(length):
    return create_hash(generate_random_str(length))


with open(file_path, 'r') as file_input, open(file_path_out, 'r') as file_output:
    str = file_input.readline()
    counter = 0
    while counter < 0 and len(str):
        hash = create_hash(str)
        file_output.write(hash + '\n')
        counter += 1
        str = file_input.readline()

    while counter < number_of_str:
        hash = create_random_str_hash(random.randint(
            size_of_string_begin, size_of_string_end))
        file_output.write(hash + '\n')
        counter += 1
        str = file_input.readline()
        
