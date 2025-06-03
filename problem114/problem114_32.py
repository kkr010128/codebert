D = int(input())
c = list(map(int,input().split()))
s = [ [0 for j in range(26)] for i in range(D)]
for i in range(D):
    tmp = list(map(int,input().split()))
    for j in range(26):
        s[i][j] = tmp[j]
t = []
for i in range(D):
    t.append(int(input()))


v = [0] * D
last = [0] * 26
sat = 0
for d in range(D):
    j = t[d] - 1
    sat += s[d][j]
    last[j] = d+1
    for j in range(26):
        sat -= c[j] * ( d + 1 - last[j] )
    v[d] = sat

for i in range(D):
    print(v[i])