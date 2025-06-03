S: str = input()
n = len(S)

if not S == S[::-1]:
    print('No')
    exit()

end = (n-1)//2
SS = S[:end]

if not SS == SS[::-1]:
    print('No')
    exit()

start = (n+3)//2 - 1
SSS = S[start:n]

if not SSS == SSS[::-1]:
    print('No')
    exit()

print('Yes')
