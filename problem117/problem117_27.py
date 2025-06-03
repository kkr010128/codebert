N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min = 0
cnt = 0
for k in b:
    min += k
j = M
for i in range(N+1):
    while(j > 0 and min > K):
        j -= 1
        min -= b[j]
    if(min > K):
        break
    cnt = max(cnt, i + j)
    if(i == N):
        break
    min += a[i]
print(cnt)
