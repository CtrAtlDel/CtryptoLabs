from parser import get_parser

parser = get_parser()
arguments = parser.parse_args()
file_path = arguments.file
encoding = arguments.encoding
crypto_functions = arguments.functions
number_of_str = arguments.number
file_out_path = arguments.output

