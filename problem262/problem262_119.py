n=int(input())
A=[]
for i in range(n):
  for _ in range(int(input())):
    x,y=map(int,input().split())
    A+=[(i,x-1,y)]
a=0
for i in range(2**n):
  if all(i>>j&1<1 or i>>x&1==y for j,x,y in A):
    a=max(a,sum(map(int,bin(i)[2:])))
print(a)