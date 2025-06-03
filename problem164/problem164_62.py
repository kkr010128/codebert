ri = [int(v) for v in input().split()]

A, B, C, D = ri

f = 1
while A > 0 and C > 0:
    if f:
        C -= B
    else:
        A -= D
    f ^= 1

print("Yes" if A > C else "No")
