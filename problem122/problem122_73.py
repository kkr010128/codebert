from collections import Counter
from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(_) for _ in stdin.readline().rstrip().split()]
CA = Counter(A)
Q = int(stdin.readline().rstrip())
ans = sum(A)
for i in range(Q):
    b, c = [int(_) for _ in stdin.readline().rstrip().split()]
    ans += (c-b)*CA[b]
    CA[c] += CA[b]
    CA[b] = 0
    print(ans)