n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
ans = len(h)

for height in h:
    if height < k:
        ans -= 1
    else:
        print(ans)
        exit()

print(ans)
