a, b, c, d = map(int, input().split())
ac = a * c
ad = a * d
bc = b * c
bd = b * d
ans_1 = max(ac,ad)
ans_2 = max(bc, bd)
ans = max(ans_1, ans_2)
print(ans)

