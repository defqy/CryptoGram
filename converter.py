#converting from bits to text
def bit2text(ct):
    global utf_bytes
    ct = ''.join(ct)
    bytes_array = [int(ct[i:i+8], 2) for i in range(0, len(ct), 8)]
    utf_bytes = bytes(bytes_array)

def hex2bin(input):
    table = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
    'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

    binary_string = ""
    input = input.lower()
    for character in input:
        binary_string += table[character]
    return binary_string

def bit2text4rus(binary):
    global text
    binary = ''.join(binary)
    bytes_array = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    utf16_bytes = bytes(bytes_array)
    decoded_text = utf16_bytes.decode('utf-16')
    text = decoded_text
    return decoded_text

def bin2hex(input):
    return format((int(input, 2)), 'x').upper()

def nbit_nbit(bit, length):
    global norm_bit
    norm_bit = []
    bits = ''.join(map(str, bit))
    for i in range(len(bits) // length):
        ot_length = bits[:length]
        norm_bit.append(ot_length)
        bits = bits.replace(ot_length, '', 1)