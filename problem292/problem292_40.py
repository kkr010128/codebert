N = int(input())
D = list(map(int,input().split()))

from itertools import combinations
counter = 0
for i in combinations(range(N),2):
    a,b = i
    counter += D[a]*D[b]
    

print(counter)