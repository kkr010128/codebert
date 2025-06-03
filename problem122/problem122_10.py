from sys import stdin
input=stdin.readline
input()
a=list(map(int,input().split()))
ans=sum(a)
b=[0]*(10**5+1)
for i in a:
  b[i]+=1
c=int(input())
for i in range(c):
  n,m=map(int,input().split())
  if b[n]>0:
    x=b[n]
    if x>0:
      b[m]+=x
      b[n]=0
      ans+=(m-n)*x
  print(ans)