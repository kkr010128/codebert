a, b = [int(x) for x in input().split()]
temp = a - 2 * b
ans = temp if temp > 0 else 0
print(ans)