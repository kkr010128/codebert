import numpy as np

n = int(input())
a = np.array(list(map(int,input().split())))

amax=max(a)+1
ah=[0]*amax

for i in a:
    for j in range(i,amax,i):
        ah[j]+=1

an=0
for i in a:
    if ah[i]==1:
        an+=1
print(an)