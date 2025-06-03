n, x, t = map(int, input().split())
i = 0
while True:
    i += 1
    if i*x >= n :
        break
print(i*t)