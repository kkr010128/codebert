import sys
input = sys.stdin.readline

n,m=map(int,input().split())
M=set(tuple(map(int,input().split())) for _ in range(m))
d={i:set() for i in range(1,n+1)}
for i,j in M:
    d[i].add(j)
    d[j].add(i)

vis=set()
res = 0
for i in range(1,n+1):
    if i not in vis:
        stack = [i]
        ans = 1
        vis.add(i)
        while stack:
            curr = stack.pop()
            for j in d[curr]:
                if j not in vis:
                    stack.append(j)
                    ans+=1
                    vis.add(j)
        res = max(ans,res)
print(res)


