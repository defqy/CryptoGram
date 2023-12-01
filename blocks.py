#splitting into blocks for encryption
def blocks_encrypt(ott, length, lang):
    global out
    out = []
    if lang == 8: ott = ott.encode('utf-8')
    elif lang == 16: ott = ott.encode('utf-16')
    ot = ''.join(format(byte, '08b') for byte in ott)
    if len(ot) % length != 0: ot += '0' * (length - len(ot) % length)
    for i in range(len(ot) // length):
        ot_length = ot[:length]
        out.append(ot_length)
        ot = ot.replace(ot_length, '', 1)

#splitting into blocks for decryption
def blocks_decrypt(ot, z):
    global out
    out = []
    for i in range(len(ot) // z):
        ot_z = ot[:z]
        out.append(ot_z)
        ot = ot.replace(ot_z, '', 1)
    out = out[::-1]