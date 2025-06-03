N = int(input())

sum_ = 0
for i in range(1, N + 1):
    n = int(N / i)
    sum_ += (n / 2) * (2 * i + (n - 1) * i)

print(int(sum_))
