import random
import string

number_of_password = 100_000 # Количество слов
size_of_string_begin = 10 # Минимальный размер строки
size_of_string_end = 15 # максимальный размер строк
file_path = "passwords.txt"

def generate_random_str(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def generate_passwords():
    with open(file_path, "w") as file:
        for i in range(0, number_of_password):
            str = generate_random_str(random.randint(size_of_string_begin, size_of_string_end))
            file.write(str +'\n')


generate_passwords()
    
