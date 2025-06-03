a = input()
for i in range(int(input())):
    b = list(input().split(' '))
    if 'print' in b:
        f = int(b[1])
        s = int(b[2])
        print(a[f:s+1])
    elif 'reverse' in b:
        f = int(b[1])
        s = int(b[2])
        a = a[:f] + a[f:s+1:][::-1] + a[s+1:]
    else:
        f = int(b[1])
        s = int(b[2])
        a = a[:f] + b[3] + a[s+1:]
