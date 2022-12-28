import argparse

import generator


BOOST = 2

MASKS = ['a', 'd', 'l', 'u']


def check_mask(mask):
    result = True
    for mask_parameter in mask:
        result &= mask_parameter in MASKS
    return result


def resolve_prf(hash):
    if len(hash) == (MD5_HASH_LEN * BOOST):
        return 'md5'
    if len(hash) == (SHA1_HASH_LEN * BOOST):
        return 'sha1'


def ords(alphabets):
    passwords_count = 1
    ords_bases = []

    for custom_alphabet in alphabets:
        passwords_count *= len(custom_alphabet)

    for i in range(len(alphabets)):
        if i == 0:
            ords_bases.append(len(alphabets[i]))
        else:
            ords_bases.append(ords_bases[i - 1] * len(alphabets[i]))

    return ords_bases, passwords_count


def brute(passwords_list, algo, nonse_1, nonse_2, hash):
    bases, passwords = ords(passwords_list)

    for password in range(passwords):
        password_word = ""
        for i in range(len(bases)):
            mask_alphabet = passwords_list[i]
            len_alphabet = len(mask_alphabet)
            if i == 0:
                password_word += mask_alphabet[password % bases[i]]
            else:
                password_word += mask_alphabet[((password * len_alphabet) // bases[i]) % len_alphabet]
        hash_r = ikev(algo, password_word.encode().hex(), nonse_1, nonse_2)
        if hash_r == hash:
            print('Password recovered! Password : ', password_word)
            return
    print('The password was not found during the enumeration.')


def ikev(mode, password, nonse_1, nonse_2):
    s_key_id = generator.get_hmac(mode, password, nonse_1).hex()
    return generator.get_hmac(mode, s_key_id, nonse_2).hex()


def rebuild_file(file):
    with open(file, "r") as f:
        text = f.read()
        text_chunks = text.split('*')
        if len(text_chunks) == 9:
            N_i = text_chunks[0]
            N_r = text_chunks[1]
            G_x = text_chunks[2]
            G_y = text_chunks[3]
            Ci = text_chunks[4]
            Cr = text_chunks[5]
            SAi = text_chunks[6]
            IDr = text_chunks[7]
            HASH_R = text_chunks[8]

            prf_type = resolve_prf(HASH_R)
            N_SECOND = G_y + G_x + Cr + Ci + SAi + IDr
            N_FIRST = N_i + N_r

            # algo, nonce_first, nonce_second, hash
            return prf_type, N_FIRST, N_SECOND, HASH_R
        else:
            print("Incorrect format file for application.")
            exit(0)


def gen_passwords(mask):
    return [alphabet(letter) for letter in mask]


def solution(mask, file):
    if check_mask(mask):
        passwords = gen_passwords(mask)
        algo, nonce_first, nonce_second, hash = rebuild_file(file)
        brute(passwords, algo, nonce_first, nonce_second, hash)
    else:
        print("Incorrect mask parameters!")
        exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.version = '1.0'
    parser.add_argument('-v',
                        '--version',
                        action='version')
    parser.add_argument('-m',
                        '--mask',
                        action='store',
                        type=str,
                        required=True,
                        help=
                        '''set the mask for password enumeration 
                            a – all latin letters (u + l) + digits; 
                            d – only digits; 
                            l – lower latin letters; 
                            u – upper latin letters. 
                        ''')
    parser.add_argument('source_file',
                        type=str,
                        action='store',
                        help='file with encrypted information. it has specified format')
    args = parser.parse_args()
    mask = args.mask
    file = args.source_file
    solution(mask, file)
