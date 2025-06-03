from bisect import bisect_left
n = int(input())
L = list(map(int, input().split()))
L.sort()

cnt = 0
for a in range(n-2):
    for b in range(a+1, n-1):
        cnt += bisect_left(L,L[a]+L[b])-(b+1)
print(cnt)