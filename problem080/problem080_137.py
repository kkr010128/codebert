N=int(input())
a,b,c,d=0,1e10,-1e10,1e10
for i in range(N):
  A,B=input().split()
  A=int(A)
  B=int(B)
  a=max(a,A+B)
  b=min(b,A+B)
  c=max(c,A-B)
  d=min(d,A-B)
print(max(abs(a-b),abs(c-d)))