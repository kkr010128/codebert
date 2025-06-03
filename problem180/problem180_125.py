N, K = map(int, input().split())

# 最小値として取りうる値は、t or K-t
t = N % K
ans = min(t, K-t)
 
print(ans)