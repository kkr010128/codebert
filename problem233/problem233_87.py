N = int(input())
P = list(map(int, input().split()))
Q = []
m = 10**17
for p in P:
    m = min(m, p)
    Q.append(m)
c = 0
for x, y in zip(P, Q):
    if x <= y:
        c += 1
print(c)
