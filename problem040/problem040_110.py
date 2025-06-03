from sys import stdin

int3 = sorted([int(x) for x in stdin.readline().rstrip().split()])
print(*int3)
