from collections import Counter
n = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2

for k in A:
    # n*(n-1)//2 - (n-1)*(n-2)//2 = n - 1
    print(ans - (cnt[k] - 1)) 
