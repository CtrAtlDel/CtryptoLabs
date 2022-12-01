from constants import BLOCK_SIZE
from constants import invSBox
from constants import sBox


def get_padding(block):
    new_block = block[:]
    length_diff = BLOCK_SIZE - len(block)
    if length_diff != 0:
        for _ in range(length_diff):
            new_block.append(0)
    return new_block


def wrapp_blocks(text):
    length = len(text)
    list_of_blocks = []
    for i in range(0, length, BLOCK_SIZE):
        block = text[i:i + BLOCK_SIZE]
        list_of_blocks.append(block)
    return list_of_blocks


def wrapp_block(data):
    new_block = data[:2]
    new_block.append(data[3])
    new_block.append(data[2])
    return new_block


def replace_block(data):
    new_block = bytearray()
    for byte in data:
        i = byte // 16
        j = byte % 16
        new_block.append(sBox[i][j])
    return new_block


def replace_iv(data):
    new_block = bytearray()
    for byte in data:
        i = byte // 16
        j = byte % 16
        new_block.append(invSBox[i][j])
    return new_block


def encrypt_block(text, key):
    data = replace_block(text)
    data = wrapp_block(data)
    encrypted_block = xor(data, key)
    return encrypted_block


def get_allround_enrypt(block, keys):
    round_zero = xor(block, keys[0])
    round_first = encrypt_block(round_zero, keys[1])
    round_second = encrypt_block(round_first, keys[2])
    return round_second


def get_allround_decrypt(block, key):
    data = xor(block, key)
    data = wrapp_block(data)
    decrypted_block = replace_iv(data)
    return decrypted_block


def delete_padding(text_decrypt):
    length = len(text_decrypt) - 1
    while text_decrypt[length] == 0:
        length -= 1
    data = text_decrypt[:length + 1]
    return data


def invert(data):
    result = data[::-1]
    for i in range(len(result)):
        result[i] = reverse_bit(result[i])
    return result


def reverse_bit(num):
    return int('{:08b}'.format(num)[::-1], 2)


def xor(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        res = bytearray(a ^ b for a, b in zip(a[len_b::], b))
        for i in range(len_a - len_b):
            res.insert(i, a[i])
        return res
    else:
        return bytearray(a ^ b for a, b in zip(a, b))
