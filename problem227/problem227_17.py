n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

s = min(k, n)
if s:
    answer = sum(h[:-s])
else:
    answer = sum(h)
print(answer)
