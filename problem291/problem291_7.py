from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
print(a - 2*b if a-2*b > 0 else 0)