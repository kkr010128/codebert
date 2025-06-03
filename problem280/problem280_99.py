from itertools import permutations
import math
n=int(input())
G=[]
for _ in range(n):
  x,y=map(int,input().split())
  G.append([x,y])
  
ans=0 
for v in permutations(range(n),n):
  for i in range(n-1):
    ans+=((G[v[i]][0]-G[v[i+1]][0])**2+(G[v[i]][1]-G[v[i+1]][1])**2)**0.5
    

print(ans/math.factorial(n))