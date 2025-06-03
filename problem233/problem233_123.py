n=int(input())
p=list(map(int,input().split()))
min_t=10**6
cnt=0
for i in range(n):
    if min_t>=p[i]:
        cnt+=1
    min_t=min(min_t,p[i])
print(cnt)