a, b, c, d = map(int, input().split())

if a % d == 0:
    mons_a = a // d
else:
    mons_a = a // d + 1

if c % b == 0:
    mons_b = c // b
else:
    mons_b = c // b + 1

if mons_a >= mons_b:
    print("Yes")
else:
    print("No")
