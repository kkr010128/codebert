n = int(input())
cif = [[0]*10 for i in range(10)]

for i in range(1, n+1):
    s = str(i)
    f = int(s[0])
    r = int(s[-1])
    cif[f][r] += 1
res = 0

for i in range(10):
    for j in range(10):
        res += cif[i][j]*cif[j][i]
print(res)