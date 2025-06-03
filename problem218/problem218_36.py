n=int(input())
d={}
for _ in range(n):
  s=input()
  if s in d:
    d[s]+=1
  else:
    d[s]=1
m=max(d.values())
ans=[]
for i,k in d.items():
  if m==k:
    ans.append(i)
for i in sorted(ans):
  print(i)