x=[]
N,A,B=map(int,input().split())
if (B-A)%2==0:
    print((B-A)//2)
else:
    c=(A-1)+(B-A+1)//2
    d=(N-B)+(B-A+1)//2
    print(min(c,d))