import sys
sys.setrecursionlimit(10**9)

k=int(input())

def dfs(keta,num):
  lunlun.append(int(num))
  if keta==10:
    return

  min_v=max(0,int(num[-1])-1)
  max_v=min(9,int(num[-1])+1)

  for i in range(min_v,max_v+1):
    dfs(keta+1,num+str(i))

lunlun=[]
for i in range(1,10):
  dfs(0,str(i))

lunlun.sort()
print(lunlun[k-1])