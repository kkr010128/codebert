X, N = list(map(int, input().split()))
if N!=0:
    P = set(list(map(int, input().split())))
else:
    print(X)
    exit(0)

dist = 100
r = None
for i in range(105, -1, -1):
    if not i in P and abs(X-i) <= dist:
        dist = abs(X-i)
        r = i

print(r)
