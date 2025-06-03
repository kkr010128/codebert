n,m=map(int,input().split())
a=0
p=0
L=[0 for _ in range(n)]
for _ in range(m):
  num,s = input().split()
  num=int(num)-1
  if not L[num] == -1:
    if s == "AC":
      a+=1
      p+=L[num]
      L[num]=-1
    else:
      L[num]+=1
print(a,p)