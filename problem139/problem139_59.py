h1, m1, h2, m2, k = map(int, input().split())

st = h1 * 60 + m1
en = h2 * 60 + m2

print(max(0, en - st - k))