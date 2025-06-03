s = input()
num = int(input())
for i in range(num):
    L = input().split()
    if L[0] == 'print':
        print(s[int(L[1]):int(L[2])+1])
    elif L[0] == 'reverse':
        ts = s[int(L[1]):int(L[2])+1]
        s = s[:int(L[1])] + ts[:: -1] + s[int(L[2])+1:]
    elif L[0] == 'replace':
        s = s[:int(L[1])] + L[3] + s[int(L[2])+1:]
