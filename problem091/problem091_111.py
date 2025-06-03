import itertools
 
N = int(input())
L = list(map(int,(input().split())))
L.sort()
Combi = list(itertools.combinations(L, 3))
count = 0
 
for i in Combi:
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])
    if((a+b)> c and a!=b != c and  a<b <c ):
        count+=1
 
print(count)