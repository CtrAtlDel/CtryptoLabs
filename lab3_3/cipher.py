from base64 import b64decode
from base64 import b64encode
import get_random

from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad


def encrypt_aes(key, data):
    iv = get_random.gen_iv(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))), iv


def encrypt_aes_iv(key, data, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'),
                                             AES.block_size)))


def encrypt_3des_iv(key, data, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'),
                                             DES3.block_size)))


def encrypt_3des(key, data):
    iv = get_random.gen_iv(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(data.encode('utf-8'), DES3.block_size))), iv


def decrypt_aes(key, data):
    raw = b64decode(data)
    cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])
    return unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)


def decrypt_3des(key, data):
    raw = b64decode(data)
    cipher = DES3.new(key, DES3.MODE_CBC, raw[:DES3.block_size])
    return unpad(cipher.decrypt(raw[DES3.block_size:]), DES3.block_size)
