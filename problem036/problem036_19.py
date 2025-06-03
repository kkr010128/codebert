from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
print(a*b, 2*(a+b))

