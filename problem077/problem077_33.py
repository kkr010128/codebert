from itertools import product
a, b, c, d = map(int, input().split())
print(max(v[0] * v[1] for v in product((a, b), (c, d))))
