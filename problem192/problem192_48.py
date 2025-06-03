from collections import Counter
n = int(input())
A = list(map(int, input().split()))


cnt = Counter(A)

ans = 0
for value in cnt.values():
    ans +=int(value*(value-1)/2)

for k in A:
    print(ans-cnt[k]+1)
