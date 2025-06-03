[N, D] = [int(i) for i in input().split()]
count = 0
for _ in range(N):
    [a, b] = [int(i) for i in input().split()]
    if a ** 2 + b ** 2 <=  D ** 2:
        count += 1
print(count)