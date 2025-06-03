import sys
input = sys.stdin.readline
INF = 10**18
def li():
    return [int(x) for x in input().split()]

N = int(input())
A = [INF] + li()
M = 1000
K = 0

for i in range(1,N+1):
    if i == N:
        sell_cnt = K
        K = 0
        M += sell_cnt * A[i]
        break
    if A[i+1] > A[i] and A[i] <= A[i-1]:
        buy_cnt = M // A[i]
        K += buy_cnt
        M -= buy_cnt * A[i]
    elif A[i+1] < A[i] and A[i] >= A[i-1]:
        sell_cnt = K
        K = 0
        M += sell_cnt * A[i]

print(M)