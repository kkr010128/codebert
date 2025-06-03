n, k = map(int, input().split())
p = list(map(int, input().split()))

for i, j in enumerate(p):
    p[i] = (j*(j+1)/2) / j 
t_sum = sum(p[:k])
ans = t_sum
for i in range(n-k):
    t_sum = t_sum - p[i] + p[i+k]
    if ans < t_sum:
        ans = t_sum
print(ans)