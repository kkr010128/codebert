h1, m1, h2, m2, k = map(int, input().split())

sm = h2*60 + m2
gm = h1*60 + m1
ans = sm - gm - k

print(ans)