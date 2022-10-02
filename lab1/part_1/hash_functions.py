from enum import Enum


class HashFunctions(Enum):
    md4 = 'md4'
    md5 = 'md5'
    sha1 = 'sha1'
    sha256 = 'sha256'
    sha512 = 'sha512'

    def str(self):
        return self.value
