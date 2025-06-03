N, K = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
ls.sort()
print(sum(ls[:K]))