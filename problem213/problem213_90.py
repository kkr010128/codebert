N = int(input())
X = list(map(int, input().split()))

total_list = []
for p in range(min(X), max(X) + 1):
    total = 0
    for x in X:
        total += (x - p) ** 2
    total_list.append(total)

print(min(total_list))