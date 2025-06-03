from itertools import accumulate
N, K = map(int, input().split())
P = [0]+list(map(int, input().split()))
Psum = list(accumulate(P))
total = 0
for i in range(K, N+1):
    if Psum[i]-Psum[i-K] > total:
        total = Psum[i]-Psum[i-K]
        index = i
ans = 0
for i in range(index, index-K, -1):
    ans += (P[i]+1)*0.5

print(ans)
