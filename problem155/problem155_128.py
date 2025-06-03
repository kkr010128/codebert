n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [True] * n
for _ in range(m):
    a, b = map(int, input().split())
    if h[a-1] > h[b-1]:
        ab[b-1] = False
    elif h[b-1] > h[a-1]:
        ab[a-1] = False
    else:
        ab[a-1] = False
        ab[b-1] = False

print(ab.count(True))