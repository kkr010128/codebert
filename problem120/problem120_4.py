N, K = map(int, input().split())
P = [int(x) for x in input().split()]
P.sort()
i = 0
k = 0

for j in P:
    if k == K:
        break
    i += j
    k += 1

print(i)