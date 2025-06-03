n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
work1=sorted([x[0] for x in l])
work2=sorted([x[1] for x in l])
if n%2==1 : 
    mmin=work1[n//2]
    mmax=work2[n//2]
else:
    mmin=work1[n//2]+work1[n//2-1]
    mmax=work2[n//2]+work2[n//2-1]
print(mmax-mmin+1)