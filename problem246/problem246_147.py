import itertools

n = int(input())
p = tuple([int(i) for i in input().split()])
q = tuple([int(i) for i in input().split()])

lst = list(itertools.permutations(list(range(1, n + 1))))
print(abs(lst.index(p) - lst.index(q)))