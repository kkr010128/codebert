n,m,l= map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for i in range(m)]
for u in range(n):
   for w in range(l):
     c=0 
     for z in range(m):
       c+=a[u][z]*b[z][w]
     if w==l-1:
       print(c)
     else:
       print(c,end=" ")
