N, M = map(int, input().split())
s = [0] * M
c = [0] * M

for i in range(M):
    s[i], c[i] = map(int, input().split())

ran = []
for i in range(10 ** (N - 1), 10 ** N):
    ran.append(i)
if N == 1:
    ran.append(0)

ran.sort()
minimum = 10 ** N
for r in ran:
    st = str(r)
    ok = True
    for j in range(M):
        if st[s[j] - 1] != str(c[j]):
            ok = False
    if ok == True:
        minimum = min(minimum, r)
        break
if minimum == 10 ** N:
    print(-1)
else:
    print(minimum)
