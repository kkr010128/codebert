n = int(input())
p = list(map(int, input().split()))

min_val = n + 1
count = 0
for x in p:
    if x < min_val:
        min_val = x
        count += 1
print(count)
