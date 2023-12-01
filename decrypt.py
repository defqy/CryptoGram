#import functions
from open_file import open_decrypt, open_key
from permutation import permutation_decrypt
from xor import xor_func
from blocks import blocks_decrypt
from converter import bit2text, hex2bin, nbit_nbit

#import arguments
import open_file
import permutation
import xor
import converter
import blocks

open_decrypt('output_encrypt.txt') #extraction ot and vector
open_key('key.txt') #extraction key
open_file.key = open_file.key.split(';') #splitting array with ";"
blocks_decrypt(hex2bin(open_file.ot), len(open_file.key)) #splitting into blocks for decryption

number_of_blocks = len(blocks.out)
blocks.out.append(open_file.vector) #adding inizalization vector
ct = [] #decrypted text

for g in range(number_of_blocks):
    permutation_decrypt(str(blocks.out[g]), open_file.key) #permutaion for decrypt
    xor_func(blocks.out[g + 1], permutation.final) #xor function
    ct.append(xor.c) #adding decrypted block

ct = ct[::-1] #turning array
nbit_nbit(ct, open_file.lang) #block length reduction function
bit2text(converter.norm_bit)
if open_file.lang == 8: text = converter.utf_bytes.decode('utf-8') #converting from bits to text for english alphabet
elif open_file.lang == 16: text = converter.utf_bytes.decode('utf-16') #converting from bits to text for russian language
open_file.key = ';'.join(map(str, open_file.key)) #join in string with ";"

#writting information in file
with open('output_decrypt.txt', 'w+') as f:
    print(f'\nDecrypted text - {text}\nInitialization vector - {open_file.vector}\nKey - {open_file.key}\n')
    f.write(f'{text}\n{open_file.vector}\n{open_file.l}')