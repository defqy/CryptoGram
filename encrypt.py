#import functions
from open_file import open_encrypt
from converter import bin_to_hex
from permutation import permutation_encrypt
from random_key import randomize
from xor import xor_func
from blocks import blocks_encrypt

#import arguments
import open_file
import random_key
import xor
import permutation
import blocks
import os

open_encrypt('input.txt') #open file open_file.path
ct = [] #array
randomize(open_file.z) #random key of length n symbols
ct.append(random_key.init_key) #adding inizalization vector
blocks_encrypt(open_file.ot, len(random_key.key), open_file.lang) #splitting into blocks for encryption
for g in range(len(blocks.out)):
    xor_func(blocks.out[g], ct[g]) #xor function
    blocks.out[g] = xor.c
    permutation_encrypt(blocks.out[g], random_key.key) #permutaion for encrypt
    ct.append(permutation.final) #adding encrypted block

random_key.key = ';'.join(map(str, random_key.key)) #converting an array to a split string

with open('key.txt', 'w+') as d: d.write(random_key.key) #writting key

ct.pop(0) #delete inizalization vector

g = ''.join(map(str, ct))
with open('output_encrypt.txt', 'w+') as f:
    print(f'\nEncrypted text - {bin_to_hex(g)}')
    print(f'Initialization vector - {random_key.init_key}\nKey - {random_key.key}\n')
    f.write(f'{bin_to_hex(g)}\n{random_key.init_key}\n{open_file.l}')

os.system('python3 sender.py')