import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X = int(input())
dp = [0]*(X+1)
dp[0] = 1
for i in range(1, X+1):
    for yen in range(100, 106):
        if yen<=i:
            if dp[i-yen]==1:
                dp[i] = 1
if dp[X]:
    print(1)
else:
    print(0)