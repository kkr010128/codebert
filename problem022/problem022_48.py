from collections import deque
import sys
input = sys.stdin.readline

_ = int(input())
S = [int(i) for i in input().strip().split()]
_ = int(input())
T = [int(i) for i in input().strip().split()]

ans = 0
for t in T:
    if t in S:
        ans += 1

print(ans)

