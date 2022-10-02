import argparse
from encoding import Encoding
from hash_functions import HashFunctions


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, metavar='file')
    parser.add_argument('-e', '--encoding', type=Encoding,
                        default=Encoding.utf8)
    parser.add_argument('-f', '--functions', type=HashFunctions,
                        default=HashFunctions.sha256)
    parser.add_argument('-n', '--number', type=int)
    parser.add_argument('-o', '--output', type=str)
    return parser
