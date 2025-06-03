import itertools
import math
N=int(input())
z=[]
for _ in range(N):
    z.append(list(map(int,input().split())))
sum=0
for per in itertools.permutations(list(range(N))):
    for i in range(N-1):
        sum+=math.sqrt((z[per[i]][0]-z[per[i+1]][0])**2+(z[per[i]][1]-z[per[i+1]][1])**2)
ans=sum/math.factorial(N)
print(ans)