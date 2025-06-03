l=[list(map(int,input().split())) for _ in range(int(input()))]
f=sorted([x+y for x,y in l])
g=sorted([x-y for x,y in l])
print(max(f[-1]-f[0],g[-1]-g[0]))