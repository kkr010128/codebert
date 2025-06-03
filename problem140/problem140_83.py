t = list(input())
tl = len(t)

for i in range(tl):
    if t[i] != '?':
        continue

    if tl == 1:
        t[i] = 'D'
    elif i == tl - 1:
        t[i] = 'D'
    elif t[i-1] == 'P':
        t[i] = 'D'
    elif t[i+1] == '?':
        t[i] = 'P'
    elif t[i+1] == 'D':
        t[i] = 'P'
    else:
        t[i] = 'D'

print(''.join(t))
