# 163 B
N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
print(N-sum(A)) if sum(A) <= N else print(-1)