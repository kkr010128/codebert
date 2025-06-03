from collections import Counter

N = int(input())
S = [input() for _ in range(N)]
cnt = Counter(S)
M = max(list(cnt.values()))
ans = []

for k, v in cnt.items():
    if v==M:
        ans.append(k)

ans.sort()

for ans_i in ans:
    print(ans_i)