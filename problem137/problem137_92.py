n=int(input())
A=[]
B=[]
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if n%2==1:
    print(B[n//2]-A[n//2]+1)
else:
    print(int(((B[n//2]+B[n//2-1])/2-(A[n//2]+A[n//2-1])/2)*2+1))

