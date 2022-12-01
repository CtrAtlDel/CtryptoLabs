## Лабораторная работа №2

Как использовать утилиту:


```bash
usage: cipher [-h] [--version] -m MODE (-e | -d) -k KEY [-i IV] [-g] file

AES encryption util

positional arguments:
  file                  File with message

optional arguments:
  -h, --help            show this help message and exit
  --version             Project version
  -m MODE, --mode MODE  Encryption or Decryption algorithm
  -e, --enc             Encryption mode
  -d, --dec             Decryption mode
  -k KEY, --key KEY     Key in hex
  -i IV, --iv IV        IV for cbc mode
  -g, --debug           Working in debug mode

```

- Утилита поддерживает 2 режима блочного шифрования CBC и ECB.
- Работает в режима шифрования и дешифрования
- Для работы в режиме cbc нужен iv вектор