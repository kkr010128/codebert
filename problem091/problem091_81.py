import itertools
n = int(input())
l = list(map(int, input().split( )))
pettern = 0
for v in itertools.combinations(l, 3):
    if v[0] != v[1] and v[1] != v[2] and v[2] != v[0]:
        if v[0]+v[1] > v[2] and v[1]+v[2] > v[0] and v[2]+v[0] > v[1]:
            pettern += 1
print(pettern)
