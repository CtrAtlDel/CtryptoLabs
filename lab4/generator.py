import argparse
import hmac

from constants import STAR, N_i, N_r, G_x, G_y, C_i, C_r, SA_i, ID_r


def get_hmac(hash_type, password, nonce):
    if hash_type == 'sha1':
        return hmac.new(bytes.fromhex(password), bytes.fromhex(nonce), "sha1").digest()
    if hash_type == 'md5':
        return hmac.new(bytes.fromhex(password), bytes.fromhex(nonce), "md5").digest()
    raise Exception("Unknown algorithm")


def solution(passdw, mode) -> None:
    s_key_id = get_hmac(args.mode, passdw.encode().hex(), N_i + N_r).hex()
    hash_hmac = get_hmac(mode, s_key_id, G_y + G_x + C_r + C_i + SA_i + ID_r).hex()
    gen_output_file(passdw, mode, hash_hmac)


def gen_output_file(passw, mode, hash_r) -> None:
    with open(passw + "_" + mode + ".txt", "w") as file:
        file.write(N_i + STAR +
                   N_r + STAR +
                   G_x + STAR +
                   G_y + STAR +
                   C_i + STAR +
                   C_r + STAR +
                   SA_i + STAR +
                   ID_r + STAR +
                   hash_r)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v',
                        '--version',
                        action='version')
    parser.add_argument('-p'
                        '--password',
                        type=str,
                        required=True,
                        help='password for encryption')
    parser.add_argument('-m',
                        '--mode',
                        type=str,
                        required=True,
                        help='set algo mode')
    args = parser.parse_args()
    passwd = args.p__password
    mode = args.mode
    solution(passwd, mode)
