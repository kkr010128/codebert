import itertools
N = int(input())
D = list(input().split())
a = itertools.combinations(D,2)
sum= 0
for i,j in a:
    sum += eval("{} * {}".format(i,j))
print(sum)