import random

def gpA(file):
    global g, p, A
    with open(file, 'r') as f:
        q = f.readlines()
        g = q[0]
        g = int(g.replace('\n', ''))
        p = q[1]
        p = int(p.replace('\n', ''))
        A = int(q[2])

def write(path, arg):
    with open(path, 'w+') as f:
        f.write(str(arg))

n = int(input('\nSender - 1\nReciever - 2\nSender recieve - 3\nClear all files (without - keyDH.txt) - 0: '))
if n == 1:
    a = random.randint(100, 1000000)
    g = random.randint(100, 1000000)
    p = random.randint(100, 1000000)

    A = g**a % p

    write('a.txt', a)
    write('gpA.txt', f'{g}\n{p}\n{A}')

elif n == 2:
    b = random.randint(100, 1000000)

    gpA('gpA.txt')

    B = g**b % p
    K = A**b % p

    write('B.txt', B)
    write('key_DH.txt', K)

elif n == 3:
    with open('B.txt', 'r') as f:
        B = f.readlines()
        B = int(B[0])
    
    gpA('gpA.txt')

    with open('a.txt', 'r') as f:
        q = f.readlines()
        a = int(q[0])

    K = B**a % p
    print(f'Key - {K}')

elif n == 0:
    arr = ['gpA.txt', 'a.txt', 'B.txt']
    for i in range(len(arr)):
        f = open(arr[i], 'r+')
        f.truncate()