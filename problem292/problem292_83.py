n = int(input())
num = list(map(int,input().split()))
a = 0
b = 0
for i in range(n):
    for j in range(n):
        a = a + num[i] * num[j]

for i in range(n):
    b = b + num[i] * num[i]

print((a - b) // 2)
