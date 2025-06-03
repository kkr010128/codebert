n=int(input())
a=list(map(int,input().split()))
q=int(input())
s=sum(a)
data=[0]*10**5
for i in a:
  data[i-1]+=1
for i in range(q):
  b,c=map(int,input().split())
  s+=(c-b)*data[b-1]
  print(s)
  data[c-1]+=data[b-1]
  data[b-1]=0
