import sys

line = sys.stdin.readline().strip().split(" ")

d = float(line[0])
t = float(line[1])
s = float(line[2])

if d / s <= t:
    print("Yes")
else:
    print("No")
