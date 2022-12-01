import argparse
import cbc
import ecb
from constants import BLOCK_SIZE

parser = argparse.ArgumentParser(prog='cipher', description='AES encryption util')
parser.add_argument('--version', action='version', version='%(prog)s 1.0',
                    help='Project version')
parser.add_argument('-m', '--mode', required=True,
                    help='Encryption or Decryption algorithm')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--enc', action='store_true', help='Encryption mode')
group.add_argument('-d', '--dec', action='store_true', help='Decryption mode')
parser.add_argument('-k', '--key', required=True, help='Key in hex')
parser.add_argument('-i', '--iv',
                    help='IV for cbc mode')
parser.add_argument('file',
                    help='File with message')

args = parser.parse_args()
mode = args.mode
file_path = args.file
key = args.key
iv = args.iv
result = None

if len(bytearray.fromhex(key)) != BLOCK_SIZE:
    raise Exception('Invalid size of key ...')

if mode == 'cbc' and iv is None:
    raise Exception('Cannot find iv in cbc mode ...')

if mode == 'cbc' and (len(iv) != BLOCK_SIZE):
    raise Exception('Invalid size of iv vector')

with open(file_path, 'r') as input_file:
    text = input_file.readline().rstrip('\n')
    if args.enc:
        if mode == 'cbc':
            result = cbc.cbc_encryption(text, bytearray.fromhex(key), bytearray.fromhex(iv))
        elif mode == 'ecb':
            result = ecb.ecb_encryption(text, bytearray.fromhex(key))
    elif args.dec:
        if mode == 'cbc':
            result = cbc.cbc_decryption(text, bytearray.fromhex(key), bytearray.fromhex(iv))
        elif mode == 'ecb':
            result = ecb.ecb_decryption(text, bytearray.fromhex(key))
    print("Done ...")
    print(result)
