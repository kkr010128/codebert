from itertools import permutations
n = int(input())
x = [i+1 for i in range(n)]
x = list(map(str, x))
pt = [''.join(p) for p in permutations(x)]
a = pt.index(''.join(input().split()))
b = pt.index(''.join(input().split()))
print(abs(a-b))