a, b, c, d = map(int, input().split())
T = 0
A = 0
while a > 0:
    a -= d
    A += 1
while c > 0:
    c -= b
    T += 1
if A >= T:
    print("Yes")
else:
    print("No")