k=int(input())
a=7
cnt=1
while cnt<=k+2:
    if a%k==0:
        print(cnt)
        flag=True
        break
    else:
        flag=False
        cnt+=1
        a=(10*a+7)%k
if not flag:
    print(-1)
