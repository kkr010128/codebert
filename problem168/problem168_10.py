N,M=map(int,input().split())
A=[]
A=list(map(int,input().split()))
if(N-sum(A)<0):
    print('-1')
    exit()
print(N-sum(A))
