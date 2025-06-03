from sys import stdin

stdin.readline().rstrip()
a = [int(x) for x in stdin.readline().rstrip().split()]
a.reverse()
print(*a)
