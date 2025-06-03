N = int(input())

T = [input() for i in range(N)]
T.sort()
c = 1
pre = T[0]
for i in range(1,N):
    if T[i] == pre:
        pass
    else:
        c += 1
    pre = T[i]
print(c)