from sys import stdin

d, t, s = [int(x) for x in stdin.readline().rstrip().split()]

print("Yes" if s * t >= d else "No")