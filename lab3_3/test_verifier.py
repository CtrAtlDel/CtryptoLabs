import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('file', type=str, action='store', help='file with text')

args = parser.parse_args()
file = args.file

params = str(file).split('_')
if len(params) < 3:
    print("false")
    exit(0)

hmac_type = None
if params[0] == 0:
    hmac_type = 'md5'
else:
    hmac_type = 'sha1'

with open(file, 'r') as ff:
    try:
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
        iv_ = bytes.fromhex(data[133:end_iv])
        text = bytes.fromhex(data[end_iv:])
        if len(text) > 4096:
            print("false")
            exit(0)
    except Exception:
        print("false")
        exit(0)

print("true")
