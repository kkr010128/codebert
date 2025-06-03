import itertools

n = int(input())
L = list(map(int, input().split()))

comb = itertools.combinations(L, 3)

ans = 0

for i in comb:
    i = list(i)
    i.sort()
    
    if i[0] + i[1] > i[2] and (i[0] != i[1] and i[1] != i[2] and i[2] != i[0]):
        ans += 1
    
print(ans)