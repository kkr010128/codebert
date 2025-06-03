n = int(input())
pair = [1, 1]

for i in range(n - 1):
    pair[i % 2] = sum(pair)

print(pair[n % 2])

