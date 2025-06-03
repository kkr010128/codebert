N=int(input())

A,B=[],[]
for i in range(N):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)

A.sort()
B.sort()

I=~-N//2
print(B[I]-A[I]+1 + (B[I+1]-A[I+1] if N%2==0 else 0))
