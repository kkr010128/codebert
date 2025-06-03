N = int(input())
num = list(range(N+1))
for i in range(3, N+1, 3):
    num[i] = 0
for i in range(5, N+1, 5):
    num[i] = 0
print(sum(num))