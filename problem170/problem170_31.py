import itertools

N, K = map(int, input().split())

num = []
for i in range(N+1):
    num.append(i)

ans = 0
for i in range(K, N+2):
    min_i = (i-1)*i//2 
    max_i = (2*N-i+1)*i//2
    ans += max_i - min_i + 1

print(ans%(10**9+7))