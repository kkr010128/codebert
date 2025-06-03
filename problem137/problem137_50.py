N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N%2!=0:
    n=(N+1)//2
    ans=B[n-1]-A[n-1]+1
else:
    n=N//2
    ans1=(A[n-1]+A[n])/2
    ans2=(B[n-1]+B[n])/2
    ans=(ans2-ans1)*2+1
print(int(ans))