# 155 A

a, b, c = input().split()

if a == b == c or (a != b and b != c and c != a):
    print("No")
else:
    print("Yes")