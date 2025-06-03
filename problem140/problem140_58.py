t = list(input())
for i in range(len(t)-1, -1, -1):
    if t[i] == '?':
        t[i] = 'D'
print(''.join(list(map(str, t))))