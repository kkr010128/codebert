import sys
input = lambda: sys.stdin.readline().rstrip()
n=int(input())
s=0 ; st=set() ; ans=[[] for i in range(n)] ; v=0
def dfs(g,v):
    global s,st,ans
    if v in st: return
    else: st.add(v)
    s+=1
    ans[v].append(s)
    for i in g[v]:
        dfs(g,i)
    s+=1
    ans[v].append(s)
g=[]
for _ in range(n):
    a=[int(i)-1 for i in input().split()]
    if a[1]==-1: g.append([])
    else: g.append(a[2:])
for i in range(n):
    if i in st : continue
    else : dfs(g,i)
for i in range(len(ans)):
    print(i+1,*ans[i])
    
    
    
