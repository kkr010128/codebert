N, M = map(int, input().split())

d = {}
flag = True

for i in range(M):
    s, c = map(int, input().split())
    if s in d.keys() and d[s] != c:
        flag = False
    d[s] = c

if M == 0:
    if N > 1: d[1] = 1
    else: d[1] = 0
elif 1 not in d.keys():
    d[1] = 1
elif N > 1 and d[1] == 0:
    flag = False

if M != 0 and max(d.keys()) > N:
    flag = False

if flag:
    res = 0
    for s, c in d.items():
        res += c * 10 ** (N - s)
    print(res)
else:
    print("-1")