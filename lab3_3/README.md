## Лабораторная работа №3

> Генератор тестов для данного протокола. Открытый текст 'SARAH WHERE IS MY TEA'  лежит в самой программе . 

```bash
usage: test_generator.py [-h] [-v] -p PASSWORD -hash {md5,sha1} -a {3des,aes-128,aes-192,aes-256}

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -p PASSWORD, --password PASSWORD
                        set the password (only 4 bytes)
  -hash {md5,sha1}, --hash {md5,sha1}
                        set the hash encryption or decryption mode
  -a {3des,aes-128,aes-192,aes-256}, --algorithm {3des,aes-128,aes-192,aes-256}
                        set the algo encryption/decryption mode
```

> Верификатор для файлов

```bash
usage: test_verifier.py [-h] [-v] file

positional arguments:
  file           file with text

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

> Утилита для подбора паролей

```bash
usage: crack.py [-h] [-v] -p PASSWORD -hash {md5,sha1} -a {3des,aes-128,aes-192,aes-256}

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -p PASSWORD, --password PASSWORD
                        set the password (only 4 bytes)
  -hash {md5,sha1}, --hash {md5,sha1}
                        set the hash encryption or decryption mode
  -a {3des,aes-128,aes-192,aes-256}, --algorithm {3des,aes-128,aes-192,aes-256}
                        set the algo encryption/decryption mode

```