import collections

def searchRoot(n):
    par = parList[n]
    if n == par:
        if len(q) > 0:
            rootIn(q,n)
        return n
    else:
        q.append(n)
        return(searchRoot(par))

def rootIn(q,root):
    while len(q) > 0:
        parList[q.popleft()] = root

n,m = list(map(int,input().split()))
q = collections.deque()

parList = [i for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    aRoot = searchRoot(a)
    bRoot = searchRoot(b)
    if aRoot != bRoot:
        parList[max(aRoot,bRoot)] = min(aRoot,bRoot)
    
#print(parList)

ansDic = dict()
rootSet = set()
for i in range(1,n+1):
    root = searchRoot(i)
    if root in rootSet:
        ansDic[root] += 1
    else:
        rootSet.add(root)
        ansDic[root] = 1

ans = 1
for i in rootSet:
    if ansDic[i] > ans:
        ans = ansDic[i]

print(ans)