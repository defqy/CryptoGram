#import functions
from open_file import open_encrypt, open_key
from converter import bin2hex
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

open_encrypt('configs/input.txt') #open file open_file.path
ct = [] #array
if open_file.key_config != '1': 
    randomize(open_file.z)
    key = random_key.key #random key of length n symbols
else:
    randomize(open_file.z)
    open_key('configs/key.txt')
    key = open_file.key
    key = key.split(';')
ct.append(random_key.init_key) #adding inizalization vector
blocks_encrypt(open_file.ot, len(key), open_file.lang) #splitting into blocks for encryption
for g in range(len(blocks.out)):
    xor_func(blocks.out[g], ct[g]) #xor function
    blocks.out[g] = xor.c
    permutation_encrypt(blocks.out[g], key) #permutaion for encrypt
    ct.append(permutation.final) #adding encrypted block

key = ';'.join(map(str, key)) #converting an array to a split string

with open('configs/key.txt', 'w+') as d: d.write(key) #writting key

ct.pop(0) #delete inizalization vector

g = ''.join(map(str, ct))
with open('configs/output_encrypt.txt', 'w+') as f:
    print(f'\nEncrypted text - {bin2hex(g)}')
    print(f'Initialization vector - {random_key.init_key}\nKey - {key}\n')
    f.write(f'{bin2hex(g)}\n{random_key.init_key}\n{open_file.l}')

os.system('python3 bot_sender.py')