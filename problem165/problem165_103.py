import collections

N = int(input())
S = []
for _ in range(N):
    S.append(input())

c = collections.Counter(S)

ans = 0
for key in c:
    ans += 1

print(ans)
