import string

def get_sub_str(letter):
    if letter == 'a':
        return list(string.ascii_letters) + list(string.digits)
    if letter == 'l':
        return list(string.ascii_lowercase)
    if letter == 'u':
        return list(string.ascii_uppercase)
    if letter == 'd':
        return list(string.digits)
