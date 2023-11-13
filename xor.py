#xor function
def xor_func(a, b):
    global c
    c = ''
    for i in range(len(b)):
        c += f'{int(a[i]) ^ int(b[i])}'