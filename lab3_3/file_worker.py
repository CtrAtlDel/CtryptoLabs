def write_file(text, algorythm, custom_hmac, psswrd, iv, nonce):
    with open(str(custom_hmac) + '_' + str(algorythm) + '_' + str(psswrd) + '.enc', 'w') as f:
        f.write('ENC')
        f.write('0' if custom_hmac == 'md5' else '1')
        if algorythm == '3des':
            flag_algorythm = '0'
        elif algorythm == 'aes-128':
            flag_algorythm = '1'
        elif algorythm == 'aes-192':
            flag_algorythm = '2'
        else:
            return '3'
        f.write(flag_algorythm)
        print("nonce: ", nonce.hex())
        f.write(nonce.hex())
        print("iv: ", iv.hex())
        f.write(iv.hex())
        print("text: ", text.hex())
        f.write(text.hex())
