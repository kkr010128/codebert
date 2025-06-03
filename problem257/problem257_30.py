n=int(input())
a=list(map(int,input().split()))
cnt=0
if 1 not in a:
    print(-1)
    exit()
else:
    num=1
    for i in range(n):
        if a[i]==num:
            num+=1
        else:
            cnt+=1
print(cnt)