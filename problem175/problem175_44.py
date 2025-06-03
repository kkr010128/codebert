import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
S = input().strip()

counter = Counter(S)
if len(counter) < 3:
    print(0)
    sys.exit()

exclude = 0
max_w = N // 2
for w in range(1, max_w+1):
    for i in range(N):
        if N <= i + 2*w:
            continue
        if S[i] != S[i+w] and S[i] != S[i+2*w] and S[i+w] != S[i+2*w]:
            exclude += 1
# print(exclude)

print(counter["R"] * counter["G"] * counter["B"] - exclude)