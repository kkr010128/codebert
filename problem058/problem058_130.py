while 1:
    a=0
    n,x=map(int,raw_input().split())
    if n==0:break
    for i in range(1,n-1):
        for j in range(i+1,n):
            c=x-i-j
            if c>j and c<=n:a+=1
    print a