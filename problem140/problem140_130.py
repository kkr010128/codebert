a = list(map(str, input().strip()))

for i in range(0, len(a)):
    if a[i] == '?':
        a[i] = 'D'
            
print(''.join(a))
