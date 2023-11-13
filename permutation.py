#permutaion for encrypt
def permutation_encrypt(message, key):
    global final
    final = ''
    for x in range(len(message)): final += message[int(key[x]) - 1]

#permutation for decrypt
def permutation_decrypt(message, key):
    global final
    final = ''
    for i in range(1, len(message) + 1): final += message[key.index(str(i))]