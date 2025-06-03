N=int(input())
lst=list(map(int,input().split(" ")))
now=0
for i in range(N):
    if lst[i]==now+1:
        now+=1
if now == 0:
    print(-1)
else:
    print(N-now)