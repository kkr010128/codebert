n=int(input())
stri=[]
time=[]

for _ in range(n):
  s,t=input().split()
  stri.append(s)
  time.append(t)
x=input()

ind=stri.index(x)

ans=0

for i in range(ind+1,n):
  ans+=int(time[i])
  
print(ans)