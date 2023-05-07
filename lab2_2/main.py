import math

rotate_amounts = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
                  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

constants = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

init_values = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

functions = 16*[lambda b, c, d: (b & c) | (~b & d)] + \
    16*[lambda b, c, d: (d & b) | (~d & c)] + \
    16*[lambda b, c, d: b ^ c ^ d] + \
    16*[lambda b, c, d: c ^ (b | ~d)]

functions_index = 16*[lambda i: i] + \
    16*[lambda i: (5*i + 1) % 16] + \
    16*[lambda i: (3*i + 5) % 16] + \
    16*[lambda i: (7*i) % 16]


def rotate_left(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32-amount))) & 0xFFFFFFFF


def rotate_right(x, amount):
    x &= 0xFFFFFFFF
    return ((x >> amount) | (x << (32 - amount)))


def create_chunk(message):
    message = bytearray(message)
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += orig_len_in_bits.to_bytes(8, byteorder='little')
    chunk = message[0:64]
    return chunk


def md5_rollback(hash, till_number, message):
    a, b, c, d = [hash[:4], hash[4:8], hash[8:12], hash[12:]]

    a = (int.from_bytes(a, byteorder='little') -
         init_values[0]) & 0xFFFFFFFF
    b = (int.from_bytes(b, byteorder='little') -
         init_values[1]) & 0xFFFFFFFF
    c = (int.from_bytes(c, byteorder='little') -
         init_values[2]) & 0xFFFFFFFF
    d = (int.from_bytes(d, byteorder='little') -
         init_values[3]) & 0xFFFFFFFF

    chunk = create_chunk(message)

    for i in range(63, till_number+3, -1):  # begins calculate from Q_59
        from_rotate = rotate_right(b - c, rotate_amounts[i])
        f = functions[i](c, d, a)
        g = functions_index[i](i)
        ch = chunk[4 * g:4 * g + 4]
        previous_a = ((from_rotate - f) -
                      constants[i]) - int.from_bytes(ch, byteorder='little') & 0xFFFFFFFF
        a, b, c, d = previous_a, c, d, a

        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        c &= 0xFFFFFFFF
        d &= 0xFFFFFFFF

    a &= 0xFFFFFFFF
    b &= 0xFFFFFFFF
    c &= 0xFFFFFFFF
    d &= 0xFFFFFFFF

    return sum(x << (32 * i) for i, x in enumerate([a, b, c, d])).to_bytes(16, 'little')


if __name__ == '__main__':
    message = "abc"
    hash = "900150983cd24fb0d6963f7d28e17f72"
    till_number = 45
    str = md5_rollback(bytes.fromhex(hash), till_number,
                       message.encode('UTF-8'))
    print(str)
