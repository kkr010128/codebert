n, q = map(int, input().split(' '))
L = []
i = 0
while i < n:
    name, time = map(str, input().split(' '))
    L.append([name, int(time)])
    i += 1
t = 0
fin = []
while len(L) != 0:
    if L[0][1] > q:
        t += q
        name = L[0][0]
        time = L[0][1] - q
        L.append([name, time])
        L.pop(0)
    else:
        t += L[0][1]
        name = L[0][0]
        time = t
        fin.append([name, time])
        L.pop(0)
ans = ''
for f in fin:
    ans += f[0] + ' ' + str(f[1]) + '\n'
print(ans[:-1])
