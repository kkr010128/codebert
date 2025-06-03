n=int(input())
l=[0]
c=0
l=l+(list(map(int,input().split())))

try:
  for i in range(1,n+1,2):
    if l[i]&1:
      c+=1
except:
  pass
print(c)