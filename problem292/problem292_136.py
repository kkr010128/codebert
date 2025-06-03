n = int(input())
d = list(map(int, input().split()))
sum = 0
count = 0

for i in d:
    count += 1
    for j in range(count, n):
        sum += i * d[j]
print(sum)