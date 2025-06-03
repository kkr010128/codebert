import sys
input = sys.stdin.readline
 
n,m=map(int,input().split())
d={i+1:[] for i in range(n)}
for i in range(m):
    x,y=map(int,input().split())
    d[x].append(y)
    d[y].append(x)
 
visit=set()
ans= 0 
for i in range(1,n+1):
    if i not in visit:
        ans+=1
        stack = [i]
        while stack:
            c=stack.pop()
            visit.add(c)
            for i in d[c]:
                if i not in visit:
                    stack.append(i)
print(ans-1)