import sys
sys.setrecursionlimit(10000000)
def dfs(s):
  if len(s)==11:
    return
  if s!="":
    a.append(int(s))
  for c in "0123456789":
    if s=="" and c=="0":continue
    if s!="":
      if abs(ord(c)-ord(s[-1]))<=1:
        dfs(s+c)
    else:
      dfs(s+c)

k=int(input())
a=[]
dfs("")
a=list(set(a))
a.sort()
print(a[k-1])


