import itertools

N = int(input())
L = list(map(int,(input().split())))
L.sort()
Combi = itertools.combinations(L, 3)
count = 0

for i, j, k in Combi:

    if((i+j)> k and i!=j!=k and  i<j <k ):
        count+=1
print(count)