from sys import stdin

a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
if a < b and b < c:
    print("Yes")
else:
    print("No")
