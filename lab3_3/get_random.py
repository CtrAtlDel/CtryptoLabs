import secrets
import string


def gen_nonce():
    result = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(64))
    return result.encode()


def gen_iv(size):
    result = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(size))
    return result.encode()
