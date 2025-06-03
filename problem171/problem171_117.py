import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))

A = [(A[i], i) for i in range(N)]
A_sort = sorted(A,reverse = True)

dp = [-float('inf')]*(N+1)
dp[0] = 0

for i in range(N):
    dp_new = [-float('inf')]*(N+1)
    pi = A_sort[i][1]  #もともといた場所
    for l in range(i+1): 
        r = i - l   #右を選んだ回数
        dp_new[l+1] = max(dp_new[l+1],dp[l] + A_sort[i][0] * (pi-l)) 
        dp_new[l] = max(dp_new[l],dp[l] + A_sort[i][0] * ((N-r-1)-pi))
    dp = dp_new
print(max(dp))