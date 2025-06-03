a=int(input())
b=list(map(int,input().split()))

n=1
result=0
for i in range(a):
    if b[i]!=n:
        result+=1
    elif b[i]==n:
        n+=1
if result==a:
    print(-1)
else:
    print(result)