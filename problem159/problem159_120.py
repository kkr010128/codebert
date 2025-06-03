m = 100
x = int(input())
y = 0
while x >= m:
    if x == m:
        break
    m = m + m // 100
    y += 1

print(y)
