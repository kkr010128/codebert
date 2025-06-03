import itertools
n = int(input())
l = list(map(int, input().split()))
count = 0
c_list = list(itertools.combinations(l, 3))

for c in c_list:
    if (c[0]+c[1])>c[2] and (c[1]+c[2])>c[0] and (c[2]+c[0])>c[1]:
        if len(set(c)) == 3:
            count += 1

print(count)