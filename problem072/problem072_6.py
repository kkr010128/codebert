N=int(input())
f=0
for i in range(N):
    a,b=map(int,input().split())
    if a==b:
        f+=1
    else:
        f=0
    
    if f==3:
        print('Yes')
        break
else:
    print('No')