#reading file for encrypt
lan = {'eng':8, 'rus':16}

def open_encrypt(file):
    global ot, z, lang, l
    with open(file, 'r') as f: 
        q = f.readlines()
        ot = q[0] #ot
        ot = ot.replace('\n', '')
        z = q[1]
        z = z.replace('\n', '')
        z = int(z) #len of key
        l = q[2]
        lang = lan[l]#language of text (for the number of bits)

#reading file for decrypt
def open_decrypt(file):
    global ot, vector, lang, l
    with open(file, 'r') as f:
        q = f.readlines()
        ot = q[0] #ot
        ot = ot.replace('\n', '')
        vector = q[1] #initialization vector
        vector = vector.replace('\n', '')
        l = q[2]
        lang = lan[l]

#reading key.txt
def open_key(file):
    global key
    with open(file, 'r') as v:
        g = v.readlines()
        key = g[0] #key