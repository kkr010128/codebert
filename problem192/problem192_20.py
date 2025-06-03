n=int(input())
a=list(map(int,input().split()))
s=[0]*n
for i in a:
  s[i-1]+=1
  
cnt=0
for i in s:
  cnt+=i*(i-1)//2
  
for i in a:
  ans=cnt
  ans-=s[i-1]-1
  print(ans)
