H, A = [int(v) for v in input().rstrip().split()]
r = int(H / A)
if H != (r * A):
    r += 1

print(r)
