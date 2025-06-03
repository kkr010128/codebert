from collections import Counter
def f(n):
    if n<2:
        return 0
    return n*(n-1)//2
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
ans = 0
for c in cnt.values():
    ans += f(c)

for a in A:
    print(ans-cnt[a]+1)