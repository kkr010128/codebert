x = int(input())
b = 100
n = 0

while b < x:
    b = b + b // 100
    n += 1

print(n)
