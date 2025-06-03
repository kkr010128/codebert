N, M = list(map(int, input().split()))

p = [0]*M
s = [0]*M
b = [0]*N
pena = 0
corr = 0

for i in range(M):
    p[i], s[i] = input().split()
    p[i] = int(p[i])
    if b[p[i]-1] != -1:
        if s[i] == "AC":
            pena += b[p[i]-1]
            corr += 1
            b[p[i]-1] = -1
        else:
            b[p[i]-1] += 1

print(corr, pena)