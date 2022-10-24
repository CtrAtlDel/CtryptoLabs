from email import parser
import multiprocessing
from parser import get_parser
from multiprocessing.dummy import Pool

from part_2.hash_functions import HashFunctions

parser = get_parser()
args = parser.parse_args()
hash_file_path = args.hash_set
dictionary_file_path = args.dictionary
encoding = args.encoding.value
hash_function_name = args.function

hashed_passwords

THREADS = multiprocessing.cpu_count()

found_passwords = []

def create_hashs(str):
    hash_obj = HashFunctions.get_hash_object()
    hash_obj.update(str.encode(encoding=encoding))
    return hash_obj.hexdigest()

def thread(hashed_passwords, chunk_of_dict):
    local_dict = dict()
    for word in chunk_of_dict:
        hashed_word = create_hashs(word)
        matches = [hash for hash in hashed_passwords if hashed_word == hash]
        if (len(matches) != 0):
            local_dict[word] = matches
    return local_dict


def init_thread(chunks):
    return thread(hashed_passwords, chunks)


def init(hashes):
    global hashed_passwords
    hashed_passwords = hashes


def init_pool(hashes):
    pool = multiprocessing.Pool(
        THREADS, initializer=init, initargs=hashes)
    return pool


def pool_thread(chunks):
    for chunk in chunks:
        result_dict = pool.apply_async(init_thread, (chunk,))
        found_passwords.append(result_dict)


with open(hash_file_path, 'r') as hash_list, open(dictionary_file_path, 'r') as dictionary_list:
    diction = dictionary_list.readline()  # берем словарь с паролями
    hash_line = hash_list.readlines()  # берем хеши
    diction = [line.strip('\n') for line in diction]
    hash_line = [line.strip('\n') for line in hash_line]
    chunk_size = int(len(hash_line)/THREADS)  # размер независимой части
    if chunk_size <= 0:
        chunk_size += 1
    chunks = [diction[i:i+chunk_size]
              for i in range(0, len(diction), chunk_size)]
    pool = init_pool(hash_line)
    pool_thread(chunks)
    pool.close()
    pool.join()

print(found_passwords)
