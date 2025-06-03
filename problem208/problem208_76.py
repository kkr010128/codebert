N, M = map(int, input().split())
scs = [tuple(map(int, input().split())) for _ in range(M)]

if N == 1:
    L, R = 0, 9
elif N == 2:
    L, R = 10, 99
else:
    L, R = 100, 999

for x in range(L, R+1):
    strX = str(x)
    for s, c in scs:
        if strX[s-1] != str(c):
            break
    else:
        print(x)
        break
else:
    print(-1)
