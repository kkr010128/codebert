n, k = list(map(int, input().split()))
h = list(map(int, input().split()))
h.sort()
if k > 0:
    h = h[:-k]
print(sum(h))