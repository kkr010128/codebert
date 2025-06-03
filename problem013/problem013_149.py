n = int(input())
min_value = 10**10
result = -(10**10)

for _ in [0]*n:
    current = int(input())
    result = max(result, current-min_value)
    min_value = min(min_value, current)

print(result)
