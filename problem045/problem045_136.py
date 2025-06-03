from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]
print("%d %d %lf" % (a/b, a%b, a/b))
