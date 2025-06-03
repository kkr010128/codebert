h = list(map(int, input().split()))

m = 0
m += 60 - h[1]
if m != 0: h[0] += 1
m += h[3] + (h[2]-h[0]) * 60
print(m-h[-1])