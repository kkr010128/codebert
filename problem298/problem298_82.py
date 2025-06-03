n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
a = 0
for hh in h:
    if hh >= k:
        a += 1
    else:
        break
print(a)
