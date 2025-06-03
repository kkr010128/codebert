a, b = map(int, input().split())

for n in range(1500):
    xa = int(n * 0.08)
    xb = int(n * 0.1)
    if a == xa and b == xb:
        print(n)
        exit()
print(-1)
