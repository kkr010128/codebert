h1, m1, h2, m2, k = map(int, input().split())
time = (h2 - h1) * 60
time += m2 - m1
print(time - k)
