X = int(input())
a = X % 100
sum = 0
for i in range(5, 0, -1):
    sum += a // i
    a %= i
if sum <= X // 100:
    print(1)
else:
    print(0)
