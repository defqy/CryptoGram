alpha = '0123456789;'

ed = int(input("Encryption - 1; Decryption - 2: "))
key = str(input("Key: "))
key = int(key[len(key)//2])
print(key)
message = input("Type the message: ")
message = message.split(;)

def caesar(alpha, ed, key, message):
    text = ''
    if ed == 1:
        alpha = alpha[-key:] + alpha[:-key]
        for i in range(len(message)): text += alpha[alpha.find(message[i])]
        print("Ciphertext - ", text)

    elif ed == 2:
        for i in range(len(message)): text += alpha[alpha.find(message[i]) + key]
        print("Decrypted text - ", text)

caesar(alpha, ed, key, message)