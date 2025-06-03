i = int(input())

x = 100000
for _ in range(i):
    x *= 1.05
    x = int((x+999) / 1000) * 1000

print(x)