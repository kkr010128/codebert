import collections
n=int(input())
a=collections.Counter(list(map(int, input().split())))
if len(a)==n: print('YES')
else: print('NO')