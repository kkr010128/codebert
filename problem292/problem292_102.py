# ABC 143 B

N = int(input())
D =[int(d) for d in input().split()]
from itertools import combinations
ans =0
for i in list(combinations(D,2)):
    ans+=i[0]* i[1]
print(ans)