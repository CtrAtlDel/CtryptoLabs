import keygen
import utils


def ecb_encryption(text, key):
    text_encr = bytearray()
    text_encr_hex = bytearray()
    keys = keygen.get_keygen(key)
    blocks = utils.wrapp_blocks(text)
    for i, block in enumerate(blocks):
        if i == len(block) - 1:  # добавляем паддинг
            block = utils.get_padding(block)
        block_encrypt = utils.get_allround_enrypt(block, keys)
        text_encr.extend(block_encrypt)
        text_encr_hex = text_encr.hex()
    return text_encr_hex


def ecb_decryption(text, key):
    text_decrypt = bytearray()
    keys = keygen.get_keygen(key)
    blocks = utils.wrapp_blocks(text)
    for i, block in enumerate(blocks):
        block_decrypt = utils.get_allround_decrypt(block, keys)
        text_decrypt.extend(block_decrypt)
    text_decrypt = utils.delete_padding(text_decrypt)
    text_decrypt_hex = text_decrypt.hex()  # удаляем паддинг
    return text_decrypt_hex
