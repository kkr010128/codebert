import sys
sys.setrecursionlimit(10**9)

k=int(input())

def dfs(keta,num):
  global ans
  ans.append(int(''.join(num)))

  if keta==10:
    return

  min_n=max(0,int(num[-1])-1)
  max_n=min(9,int(num[-1])+1)
  for i in range(min_n,max_n+1):
    dfs(keta+1,num+[str(i)])

ans=[]
for i in range(1,10):
  dfs(1,[str(i)])

ans.sort()
print(ans[k-1])