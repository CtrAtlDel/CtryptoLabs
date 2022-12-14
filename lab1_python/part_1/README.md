## Part_1

Утилита позволяет сгенерировать хеш-значения для списка паролей.

> Поддерживаемые режимы кодировки 
> 1. ascii
> 2. utf8
> 3. utf16le
> 4. utf16be

> Поддерживаемые хеш функции
> 1. md4
> 2. md5
> 3. sha1
> 4. sha256
> 5. sha512

Значение по умолчанию для кодировки UTF-8

Запуск утилиты:
```shell
$ hash_gen.py [-e ENCODING] [-f HASH_FUNCTIONS] [-n NUMBER_OF_WORDS] [-o OUTPUT_FILE] file n
```

Пример запуска утилиты:
```shell
$  python3 main.py -f=sha256 -e=utf8 -o=./output.txt --file=./input.txt -n=2
```
Опции для утилиты:
    - '-e' кодировка (см поддерживаемы кодировки) 
    - '-o' файл для записи результата программы 
    - '-f' название криптографической хеш функции (см поддерживаемы хеш функции) 
    - '-n' количество хеш-значений в выходном файле