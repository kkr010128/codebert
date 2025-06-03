a, b, c, d = map(int, input().split())

ac = a * c
ad = a * d
bc = b * c
bd = b * d

max_a = max(ac, ad)
max_b = max(bc, bd)

print(max(max_a, max_b))
