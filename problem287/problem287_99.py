n = int(input())
print('Yes' if any(i*j == n for i in range(1, 10) for j in range(1, 10)) else 'No')