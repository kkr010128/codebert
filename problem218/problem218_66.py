from collections import defaultdict

N = int(input())
S = defaultdict(int)
for i in range(N):
    S[input()] += 1
m = max(S.values())
for s in sorted(filter(lambda x: S[x] == m, S)):
    print(s)