n = int(input())
(*a, ) = map(int, input().split())
q = int(input())
(*m, ) = map(int, input().split())
s = set()
for j in range(2 << n):
    c = 0
    for k in range(n):
        if j >> k & 1:
            c += a[k]
    s.add(c)

for i in m:
    print("yneos"[i not in s::2])
