n,m,k = map(int,input().split())
ans = 0
g = [[i for i in input()] for i in range(n)]

for maskY in range(1 << n):
   ng = [[0]*m for i in range(n)]
   for bit in range(n):
       if maskY & (1 << bit):
           for i in range(m):
               ng[bit][i] = 1
   for maskX in range(1 << m):
       ngg = [[i for i in j] for j in ng]
   #    print(ngg)
       for bit in range(m):
           if maskX & (1 << bit):
               for i in range(n):
                   ngg[i][bit] = 1
       cnt = 0
       for y in range(n):
           for x in range(m):
               if g[y][x]=="#" and ngg[y][x]==0:
                   cnt += 1
   #    print(cnt)
       if cnt == k:
           ans += 1
print(ans)