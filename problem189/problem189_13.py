n, m = map(int, input().split())
count = 0

# [2, 0]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        count += 1
# [0, 2]
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        count += 1

print(count)
