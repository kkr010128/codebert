from sys import stdin

a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
print(len([x for x in range(a, b+1) if c % x == 0]))
