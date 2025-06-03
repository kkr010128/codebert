import itertools
n = int(input())
l = list(map(int,input().split()))
count = 0
for item in itertools.combinations(l, 3):
    if len(set(item)) == 3:
        if item[0] + item[1] > item[2] and item[1] + item[2] > item[0] and item[2] + item[0] > item[1]:
            count += 1
print(count)