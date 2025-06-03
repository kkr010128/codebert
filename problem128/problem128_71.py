X, N = list(map(int, input().split()))
p = set(map(int, input().split()))

dist = 0

if N == 0:
    print(X)
    dist_max = -2
else:
    dist_max = max(abs(max(p) - X), abs(min(p) - X))

while dist <= dist_max+1:
    if (X - dist in p) and (X + dist in p):
        dist += 1
        continue

    if not (X - dist in p):
        print(X - dist)
        break
    elif not (X + dist in p):
        print(X + dist)
        break