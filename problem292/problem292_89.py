n = int(input())
D = list(map(int, input().split()))
sum = 0
for i in range(n):
    for j in range(n):
        if i != j:
            sum += D[i] * D[j]
print(sum // 2)