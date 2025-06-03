n = int(input())
dp = [1, 1]
for i in range(2, n + 1):
    dp = [dp[-1], dp[-2] + dp[-1]]
print(dp[-1])
