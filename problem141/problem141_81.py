import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
low = [0]*(N+1)
high = [0]*(N+1)
low[N] = A[N]
high[N] = A[N]

for i in range(N-1, -1, -1):
    low[i] = (low[i+1]+1)//2+A[i]
    high[i] = high[i+1]+A[i]

if not low[0]<=1<=high[0]:
    print(-1)
    exit()

ans = 1
now = 1

for i in range(N):
    now = min(2*(now-A[i]), high[i+1])
    ans += now

print(ans)