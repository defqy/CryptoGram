import random_key

try: 
    random_key.randomize(int(input('Type the key length or click "Enter"(256 bits by default): ')))
except: 
    random_key.randomize(256)

key = ';'.join(map(str, random_key.key))

with open('configs/key.txt', 'w+') as d: 
    d.write(key)
print('Success!')