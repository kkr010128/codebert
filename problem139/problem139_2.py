h1, m1, h2, m2, k = list(map(int, input().split()))

okiteru = h2 * 60 + m2 - (h1 * 60 + m1)
print(okiteru - k)
