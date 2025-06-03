from statistics import median
n=int(input())
A,B=[],[]
for _ in range(n):
  a,b=map(int,input().split())
  A.append(a*2)
  B.append(b*2)
ma,mb = int(median(A)),int(median(B))
#print(ma,mb)
if n%2 == 0:
  print(mb-ma+1)
else:
  print((mb-ma)//2+1)
