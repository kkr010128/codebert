n = int(input())
print(sum((n - 1) // i for i in range(1, n)))