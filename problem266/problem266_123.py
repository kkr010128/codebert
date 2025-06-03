import itertools
a = [0, 1, 2, 3, 4, 5]
x = int(input())
n = x // 100
m = x % 100
for c in itertools.combinations_with_replacement(a, n):
    if sum(c) == m:
        print(1)
        break
else:
    print(0)