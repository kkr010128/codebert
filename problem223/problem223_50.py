N,K = map(int,input().split())
A = list(map(int,input().split()))
wa = [0] * (N+1)
for i in range(N):
    wa[i+1] = wa[i] + (A[i]+1)/2
Max = 0
for i in range(N-K+1):
    Max = max(Max,wa[K+i]-wa[i])
print(Max)
