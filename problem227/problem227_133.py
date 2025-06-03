N, K = map(int, input().split())
h = list(map(int, input().split()))

h = sorted(h)
if K == 0:
    print(sum(h))
else:
    print(sum(h[:-K]))