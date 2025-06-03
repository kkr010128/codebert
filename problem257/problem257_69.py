N=int(input())
alst=list(map(int,input().split()))

i=1
for a in alst:
    if a==i:
        i+=1
i-=1

if i>0:
    print(N-i)
else:
    print(-1)