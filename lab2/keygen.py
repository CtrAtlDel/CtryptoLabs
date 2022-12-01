import utils


def get_keygen(key_zero):
    key_list = []
    key_one = utils.invert(key_zero)
    key_two = utils.xor(key_zero, key_one)
    key_list.append(key_zero)
    key_list.append(key_one)
    key_list.append(key_two)
    return key_list
