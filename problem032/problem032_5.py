import math

n = int(input())
vector_x = [float(x) for x in input().split(" ")]
vector_y = [float(y) for y in input().split(" ")]

p1 = sum([abs(x - y) for x, y in zip(vector_x, vector_y)])
p2 = sum([abs(x - y) ** 2 for x, y in zip(vector_x, vector_y)]) ** (1/2)
p3 = sum([abs(x - y) ** 3 for x, y in zip(vector_x, vector_y)]) ** (1/3)
t = max([abs(x - y) for x, y in zip(vector_x, vector_y)])

print("{:.6f}".format(p1))
print("{:.6f}".format(p2))
print("{:.6f}".format(p3))
print("{:.6f}".format(t))