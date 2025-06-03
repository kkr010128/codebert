N = int(input())
X = list(map(int,input().split()))
cmin = 10**6+10
for i in range(101):
    cnt = 0
    for j in range(N):
        cnt += (i-X[j])**2
    cmin = min(cmin,cnt)
print(cmin)