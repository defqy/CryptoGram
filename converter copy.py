#converting from bits to text
def bit2text(ct):
    global text
    text = ''
    for i in range(len(ct)):
        input_string=int(ct[i], 2)
        Total_bytes= (input_string.bit_length() +7) // 8
        input_array = input_string.to_bytes(Total_bytes, "big")
        ASCII_value=input_array.decode()
        text += ASCII_value
    return text

print(bit2text(['0110101100010000', '0100001100101000', '0000001000011100', '1000011111110001']))

def hex_to_bin(input):
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

def bin_to_hex(input):
    return format((int(input, 2)), 'x').upper()

def nbit_nbit(bit, length):
    global norm_bit
    norm_bit = []
    bits = ''.join(map(str, bit))
    for i in range(len(bits) // length):
        ot_length = bits[:length]
        norm_bit.append(ot_length)
        bits = bits.replace(ot_length, '', 1)

nbit_nbit()