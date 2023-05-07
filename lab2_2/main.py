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
    message += b'\x80'
    message_len_bits = (8 * len(message)) & 0xffffffffffffffff
    padding_len = (64 - (len(message) % 64)) % 64
    padding = b'\x00' * padding_len
    return message + padding + message_len_bits.to_bytes(8, byteorder='little')


def md5_rollback(hash, till_number, message):
    a, b, c, d = [int.from_bytes(hash[i:i+4], byteorder='little') for i in range(0, 16, 4)]

    a, b, c, d = (a - init_values[0]) & 0xFFFFFFFF, (b - init_values[1]) & 0xFFFFFFFF, \
                 (c - init_values[2]) & 0xFFFFFFFF, (d - init_values[3]) & 0xFFFFFFFF

    chunk = create_chunk(message)

    for i in range(63, till_number + 2, -1):
        g = functions_index[i](i)
        ch = chunk[4 * g:4 * g + 4]
        a, b, c, d = (d, a, b, c)
        f = functions[i](c, d, a)
        from_rotate = rotate_right(b - c, rotate_amounts[i])
        a = ((from_rotate - f - constants[i] - int.from_bytes(ch, byteorder='little')) & 0xFFFFFFFF)
        
    return sum(x << (32 * i) for i, x in enumerate([a, b, c, d])).to_bytes(16, 'little')


if __name__ == '__main__':
    message = "abc"
    hash = "900150983cd24fb0d6963f7d28e17f72"
    till_number = 45
    str = md5_rollback(bytes.fromhex(hash), till_number,
                       message.encode('UTF-8'))
    print(str)
