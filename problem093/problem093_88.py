n,k = map(int,input().split())
p = list(map(int,input().split()))
c = list(map(int,input().split()))

for i in range(n):
    p[i] -= 1

v = [False] * n
roop = []

for i in range(n):
    if not v[i]:
        tmp = [i]
        while True:
            t = p[tmp[-1]]
            v[t] = True
            if tmp[0] == t:
                break
            else:
                tmp.append(t)
        roop.append(tmp)

s = []

for li in roop:
    s1 = 0
    for i in li:
        s1 += c[i]
    s.append(s1)

s2 = []

for li in roop:
    tmp = [0]
    for i in li:
        tmp.append(tmp[-1] + c[i])
    for i in li:
        tmp.append(tmp[-1] + c[i])
    s2.append(tmp)

v2 = [-1] * n

for i,li in enumerate(roop):
    for j in li:
        v2[j] = i

ans = -10**20

for i,li in enumerate(roop):
    t = -10**20
    if s[i] <= 0:
        for j in range(len(li)):
            for k1 in range(j+1, j + 1 + min(k, len(li))):
                t = max(t, s2[i][k1] - s2[i][j])
        ans = max(ans, t)
    else:
        for cnt in range(min(len(li), k)+1):
            for j in range(len(li)):
                if k >= cnt:
                    t = max(t, s2[i][cnt+j] - s2[i][j] + s[i] * ((k - cnt) // len(li)))
        ans = max(ans, t)

print(ans)
