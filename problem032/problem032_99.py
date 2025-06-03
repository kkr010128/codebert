import math

n = int(input())
xv = [int(xi) for xi in input().split()]
yv = [int(yi) for yi in input().split()]

print(sum([abs(xi-yi) for (xi, yi) in zip(xv, yv)]))
print(math.sqrt(sum([pow(abs(xi-yi), 2) for (xi, yi) in zip(xv, yv)])))
print(math.pow(sum([pow(abs(xi-yi), 3) for (xi, yi) in zip(xv, yv)]), 1/3))
print(max([abs(xi-yi) for (xi, yi) in zip(xv, yv)]))