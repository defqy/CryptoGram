import random

n = int(input('Sender - 1; Reciever - 2; Sender recieve - 3; Clear all files (without - keyDH.txt) - 0: '))
if n == 1:
    a = random.randint(100, 1000000)
    g = random.randint(100, 1000000)
    p = random.randint(100, 1000000)

    A = g**a % p

    with open('a.txt', 'w+') as f:
            f.write(f'{a}')

    with open('gpA.txt', 'w+') as f:
        f.write(f'{g}\n{p}\n{A}')

elif n == 2:
    b = random.randint(100, 1000000)
    with open('gpA.txt', 'r') as f:
        q = f.readlines()
        g = q[0]
        g = int(g.replace('\n', ''))
        p = q[1]
        p = int(p.replace('\n', ''))
        A = int(q[2])

    B = g**b % p
    K = A**b % p

    with open('B.txt', 'w+') as f:
        f.write(f'{B}')

    with open('key_DH.txt', 'w+') as f:
        f.write(f'{K}')

elif n == 3:
    with open('B.txt', 'r') as f:
        B = f.readlines()
        B = int(B[0])
    
    with open('gpA.txt', 'r') as f:
        q = f.readlines()
        g = q[0]
        g = int(g.replace('\n', ''))
        p = q[1]
        p = int(p.replace('\n', ''))
        A = int(q[2])

    with open('a.txt', 'r') as f:
        q = f.readlines()
        a = int(q[0])

    K = B**a % p
    print(f'Key - {K}')

elif n == 0:
    f = open('gpA.txt', 'r+')
    f.truncate()
    z = open('a.txt', 'r+')
    z.truncate()
    o = open('B.txt', 'r+')
    o.truncate()