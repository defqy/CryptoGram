# def blocks_encrypt(ott, length, lang): #ot = butterfly, length = 12
#     global out, ot
#     out = []
#     if lang == 8: ot = ''.join(format(ord(i), '08b') for i in ott)
#     elif lang == 16: ot = ''.join(format(x, 'b') for x in bytearray(ott, 'utf-8'))
#     print(ot)
#     if len(ot) % length != 0: ot += '0' * (length - len(ot) % length)
#     for i in range(len(ot) // length):
#         ot_length = ot[:length]
#         out.append(ot_length)
#         ot = ot.replace(ot_length, '', 1)
#     print(f'OUT - {out}')

# blocks_encrypt('qwerty', 12, 8)

# st_rus = 'привет'
# out2 = ' '.join(format(x, 'b') for x in bytearray(st_rus, 'utf-8'))
# out2 = out2.replace(' ', '')

# if out2 == ot: print('ok')
# else:print('no')

# print(f'{out2}')

lan = {'eng':8, 'rus':16}
print(lan)