import argparse
from encoding import Encoding
from hash_functions import HashFunctions

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dictionary', type=str, metavar='dictionary_file_path')
    parser.add_argument('hashset', type=str, metavar='hash_file')
    parser.add_argument('-e', '--encoding', type=Encoding,
                        default=Encoding.utf8)
    parser.add_argument('-f', '--function', type=HashFunctions, 
                        default=HashFunctions.sha256)