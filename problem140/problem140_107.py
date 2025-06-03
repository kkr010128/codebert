t = list(input())
a = 0
b = 0

for i in range(len(t)):
    if i == 0 and t[i] == '?':
        t[i] = 'D'
    
    if 0 < i < len(t) - 1 and t[i] == '?':
        if t[i-1] == 'P':
            t[i] = 'D'
        elif t[i+1] == 'P':
            t[i] = 'D'
        else:
            t[i] = 'P'

    if i == len(t) -1 and t[i] == '?':
        t[i] = 'D'

print(''.join(t))