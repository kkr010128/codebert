n = int(input())
a = list(map(int, input().split()))
x = 0
b = [0] * n
for i in range(n):
    b[a[i] - 1] += 1

x = 0
for j in range(n):
    x += ((b[j] - 1) * b[j] / 2)

for k in range(n):
    print(int(x - b[a[k] - 1] + 1))