X, N = map(int, input().split())
P = list(map(int, input().split()))
st = set(P)
ans = 111
for i in range(111):
    if i in st:
        continue
    if abs(ans - X) > abs(i - X):
        ans = i
print(ans)
