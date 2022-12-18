import argparse
import cipher
import custom_hmac
import file_worker
import get_random

CONST_WORLDS = 'SARAH WHERE IS MY TEA'

ALGO_NUMBER = {'3des': 16, 'aes-128': 16, 'aes-192': 24, 'aes-256': 32}

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-p', '--password', action='store', type=str,
                    required=True,
                    help='set the password (only 4 bytes)')
parser.add_argument('-hash', '--hash', action='store', type=str,
                    required=True, help='set the hash encryption or decryption mode ',
                    choices=['md5', 'sha1'])
parser.add_argument('-a', '--algorithm', action='store', required=True,
                    type=str,
                    help='set the algo encryption/decryption mode ',
                    choices=['3des', 'aes-128', 'aes-192', 'aes-256'])


def get_key_nonce(passwd, hmac_type, key_size):
    custom_nonce = get_random.gen_nonce()
    if hmac_type == 'sha1':
        type_hmac = custom_hmac.HashType.SHA1
    else:
        type_hmac = custom_hmac.HashType.MD5
    hmac = custom_hmac.create_hmac(key_size, type_hmac, passwd, custom_nonce)
    return hmac, custom_nonce


args = parser.parse_args()
password = args.password
algorithm = args.algorithm
hsh = args.hash

if len(password) != 8:
    raise Exception('Incorrect length password')

pwd = password
password = bytearray.fromhex(password)
key, nonce = get_key_nonce(password, hsh, ALGO_NUMBER[algorithm])
if algorithm == '3des':
    encrpt, iv = cipher.encrypt_3des(key, CONST_WORLDS)
else:
    encrpt, iv = cipher.encrypt_aes(key, CONST_WORLDS)
file_worker.write_file(encrpt, algorithm, hsh, pwd, iv, nonce)
