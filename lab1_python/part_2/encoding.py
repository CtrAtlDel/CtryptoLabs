from enum import Enum


class Encoding(Enum):
    ascii = 'ascii'
    utf8 = 'utf8'
    utf16le = 'utf-16-le'
    utf16be = 'utf-16-be'

    def str(self):
        return self.value
