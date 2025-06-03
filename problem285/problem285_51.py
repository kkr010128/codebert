import numpy as np

S = list(map(str, input().rstrip()))

ans = np.zeros(len(S) + 1, dtype=np.int64)

# 左から、右から流す
for i, s in enumerate(S):
    if s == "<":
        ans[i+1] = max(ans[i+1], ans[i]+1)

ans = ans[::-1]

for i, s in enumerate(S[::-1]):
    if s == ">":
        ans[i+1] = max(ans[i+1], ans[i]+1)

print(ans.sum())