a, b, n = map(int, input().split())
print(a * ((b - 1, n)[n <= b - 1] % b) // b)