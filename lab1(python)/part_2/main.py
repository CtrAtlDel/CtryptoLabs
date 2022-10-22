from email import parser
import multiprocessing
from parser import get_parser
from multiprocessing.dummy import Pool

THREADS = multiprocessing.cpu_count()

parser = get_parser()
args = parser.parse_args()
hash_file_path = args.hash_set
dictionary_file_path = args.dictionary
encoding = args.encoding.value
hash_function_name = args.function

with open(hash_file_path, 'r') as hash_list, open(dictionary_file_path, 'r') as dictionary_list:
    diction = dictionary_list.readline()
    hash_line = hash_list.readlines()
    diction = [line.strip('\n') for line in diction]
    hash_line = [line.strip('\n') for line in hash_line]
    chunk_size = int(len(hash_line)/THREADS)
    if chunk_size <= 0:
        chunk_size += 1
    chunks = [diction[i:i+chunk_size]
              for i in range(0, len(diction), chunk_size)]
    pool = multiprocessing.Pool(THREADS, ) # fix

    for chunk in chunks:
        new_diction = pool.apply_async() # fix
    pool.close()
    pool.join()