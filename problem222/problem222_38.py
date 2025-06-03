import collections
N = int(input())
lsA = list(map(int,input().split()))

cout = collections.Counter(lsA)
ans = 'YES'
for i in cout.values():
    if i > 1:
        ans = 'NO'
        break

print(ans)