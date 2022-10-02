import enum


class HashFunctions(enum):
    md4 = 'md4'
    md5 = 'md5'
    sha1 = 'sha1'
    sha256 = 'sha256'
    sha512 = 'sha512'

    def str(self):
        return self.value


class Encoding(enum):
    ascii = 'ascii'
    utf8 = 'utf8'
    utf16le = 'utf-16-le'
    utf16be = 'utf-16-be'

    def str(self):
        return self.value
