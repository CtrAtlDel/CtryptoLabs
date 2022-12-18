import argparse
import pathlib

import cipher
import cracker
from test_generator import get_key_nonce

KEY_SIZES = {'3des': 16, 'aes-128': 16, 'aes-192': 24, 'aes-256': 32}
ALGO_NUMBER = {'0': '3des', '1': 'aes-128', '2': 'aes-192', '3': 'aes-256'}
HMAC_NUMBER = {'0': 'md5', '1': 'sha1'}

CONST_WORLDS = 'SARAH WHERE IS MY TEA'

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path, action='store', help='file with encrypted text')
args = parser.parse_args()
filepath = args.file

params = str(filepath).split('_')
hmac = params[0]
algo = params[1]
password = params[2][0:4]
with open(filepath, 'r') as ff:
    data = ff.read()
    message = data[0:3]
    hmac_algo = data[3]
    cipher_algo = data[4]
    nonce = bytes.fromhex(data[5:133])
    size_iv = None
    if cipher_algo == '0':
        size_iv = 8
    else:
        size_iv = 16
    end_iv = 133 + size_iv * 2
    iv_ = bytes.fromhex(data[133:end_iv])  # iv from file
    text = bytes.fromhex(data[end_iv:])  # text from file

cipher_text = bytes()
password_guess = bytes([0x00, 0x00, 0x00, 0x00])
ciphertext = text.decode()

counter = 0
while ciphertext != cipher_text.decode():
    key = get_key_nonce(password, hmac, KEY_SIZES[params[1]])
    if algo == '3des':
        encrypt_text = cipher.encrypt_3des_iv(key, CONST_WORLDS, iv_)
        message = cipher.decrypt_3des(key, encrypt_text).decode()
    else:
        encrypt_text = cipher.encrypt_aes_iv(key, CONST_WORLDS, iv_)
        message = cipher.decrypt_aes(key, encrypt_text).decode()
    pswd = cracker.trace_gen(password_guess, 1)
    print("password: " + pswd)
    counter += 1

    if ciphertext == cipher_text.decode():
        print("message: ", message)
        print("password: ", cracker.trace_gen(password_guess, -1).hex())