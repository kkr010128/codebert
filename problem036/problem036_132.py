from sys import stdin

a, b = (int(x) for x in stdin.readline().rstrip().split())

area, perimeter = a * b, (a + b) * 2

print(area, perimeter)

