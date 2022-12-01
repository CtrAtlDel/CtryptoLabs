import keygen
import utils


def cbc_encryption(text, key, iv):
    text_encr = bytearray()
    text_encr_hex = bytearray()
    keys = keygen.get_keygen(key)
    blocks = utils.wrapp_blocks(text)
    iv_xor = iv
    for i, block in enumerate(blocks):
        if i == len(blocks) - 1:
            block = utils.get_padding(block)
        block_xor = utils.xor(iv_xor, block)
        block_encrpt = utils.get_allround_enrypt(block_xor, keys)
        iv_xor = block_encrpt
        text_encr.extend(block_encrpt)
        text_encr_hex = text_encr.hex()
    return text_encr_hex


def cbc_decryption(text, key, iv):
    text_decrypt = bytearray()
    keys = keygen.get_keygen(key)
    blocks = utils.wrapp_blocks(text)
    iv_xor = iv
    for i, block in enumerate(blocks):
        block_decrypt = utils.get_allround_decrypt(block, keys)
        block_xor = utils.xor(iv_xor, block_decrypt)
        iv_xor = block
        text_decrypt.extend(block_xor)
    text_decrypt = utils.delete_padding(text_decrypt)
    text_decrypt_hex = text_decrypt.hex()
    return text_decrypt_hex
