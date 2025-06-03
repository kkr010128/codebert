N = int(input())
L = []
for i in range(N):
    s, t = input().split()
    L.append((s, int(t)))
X = input()

ans = 0
f = False
for s, t in L:
    if f:
        ans += t
    if s == X:
        f = True
print(ans)
