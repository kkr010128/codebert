import sys
s = sys.stdin.readlines
A, V = [int(x) for x in input().split()]
B, W= [int(x) for x in input().split()]
T = int(input())

d = abs(A - B)
d2 = (V - W) * T
s = 'YES' if d <= d2 else 'NO'
print(s)

