N = int(input())
P = list(map(int, input().split()))

mini = 10 ** 9
count = 0
for i in range(N):
    if P[i] <= mini:
        mini = P[i]
        count += 1
print(count)