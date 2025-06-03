v = 100000
for _ in [0]*int(input()):
    v *= 1.05
    v += 1000 * (v%1000 > 0)
    v -= v%1000
print(int(v))