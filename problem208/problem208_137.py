n, m = map(int, input().split())
nl = [i for i in range(1000)]
if m == 0:
    for i in range(1000):
        st = str(i)
        if len(st) != n:
            nl[i] = 1000
    print(min(nl) if min(nl) < 1000 else -1)
    exit()
for h in range(m):
    s, c = map(int, input().split())
    for i in range(1000):
        st = str(i)
        if len(st) != n or st[s - 1] != str(c):
            nl[i] = 1000
print(min(nl) if min(nl) < 1000 else -1)