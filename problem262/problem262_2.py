def popcount(x):
    x = (x & 0x5555555555555555) + (x >> 1  & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2  & 0x3333333333333333)
    x = (x & 0x0f0f0f0f0f0f0f0f) + (x >> 4  & 0x0f0f0f0f0f0f0f0f)
    x = (x & 0x00ff00ff00ff00ff) + (x >> 8  & 0x00ff00ff00ff00ff)
    x = (x & 0x0000ffff0000ffff) + (x >> 16 & 0x0000ffff0000ffff)
    x = (x & 0x00000000ffffffff) + (x >> 32 & 0x00000000ffffffff)
    return x
n = int(input())

testimonies = [[] * n for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        testimonies[i].append((x-1, y))

ans = 0
for bits in range(1, 1<<n):
    possible = True
    for i in range(n):
        if not bits >> i & 1:
            continue
        for x, y in testimonies[i]:
            if bits >> x & 1 != y: 
                possible = False
                break
        if not possible:
            break
    if possible:
        ans = max(ans, popcount(bits))
print(ans)