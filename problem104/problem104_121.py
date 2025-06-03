l, r, d = map(int, input().split())
count = 0

for i in range(1, 101):
    temp = i * d
    if l <= temp and temp <= r:
        count += 1
    elif temp > r:
        break

print(count)
