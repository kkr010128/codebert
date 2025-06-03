while 1:
    ans=0
    n,x=map(int,raw_input().split())
    if n:
        for i in range(1,n-1):
            for j in range(i+1,n):
                for k in range(j+1,n+1):
                    if i+j+k==x:ans+=1
    else:break
    print ans