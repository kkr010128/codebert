import sys

alpha = input()

text = 'abcdefghijklmnopqrstuvwxyz'

for k in range(26):
    if text[k] == alpha:
        print('a')
        sys.exit()
    else:
        if k == 25:
            print('A') 