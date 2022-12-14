import hmac
from enum import Enum


class HashType(Enum):
    MD5 = 0
    SHA1 = 1


def create_hmac(key_size, hash_type, passwd, nonce):
    custom_hmac = hmac_enc(hash_type, passwd, nonce)

    if len(custom_hmac) > key_size:
        return custom_hmac[0:key_size]  # возвращаем первые key_size элементов из hmac
    elif len(custom_hmac) < key_size:
        another = hmac_enc(hash_type, passwd, custom_hmac)
        return (custom_hmac + another)[0:key_size]
    else:
        return custom_hmac


def hmac_enc(hash_type, password, nonce):  # берем встроенный hmac
    if hash_type == HashType.SHA1:
        return hmac.new(password, nonce, "sha1").digest()
    else:
        return hmac.new(password, nonce, "md5").digest()
