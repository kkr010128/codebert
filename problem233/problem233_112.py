n = int(input())
p = list(map(int,input().split()))
m = n
q = 2 * (10 ** 5)

for i in range(n):
    q = min(p[i],q)
    if not p[i] <= q:
        m -= 1

print(m)