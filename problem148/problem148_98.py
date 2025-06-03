a, b, c, k = map(int, input().split())

count = 0
if a < k:
    count += a
    if a+b < k:
        count -= k-a-b
else:
    count = k

print(count)