# coding: utf-8
alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = ''
while True:
    try:
        n = input()
        S += n
    except EOFError:
        break
ans_dict = {}
for char in alphabet:
    ans_dict[char] = S.count(char)
    ans_dict[char] += S.count(char.upper())
for k, v in sorted(ans_dict.items(), key=lambda x: x[0]):
    print('{} : {}'.format(k, v))