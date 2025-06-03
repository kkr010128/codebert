import sys
sys.setrecursionlimit(100000000)
k=int(input())
logl=len(str(k))

def bfs(nowres, result=[]):
  if len(result) >= k:
    return sorted(result)
  rescand=[]
  for res in nowres:
    eq=res*10+res%10
    rescand.append(eq)
    if eq % 10>0:
      rescand.append(eq-1)
    if eq % 10<9:
      rescand.append(eq+1)
  return bfs(rescand, result+nowres)

res=bfs(list(range(1,10)))
#print(res)
print(res[k-1])