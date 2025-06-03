chs = 'abcdefghijklmnopqrstuvwxyz'
s = input()
for i,c in enumerate(chs):
    if s == c:
        print(chs[i+1])
        break