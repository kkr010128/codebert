n = list(map(int, input().split()))
result = "Yes" if sum(n) % 9 == 0 else "No"
print(result)