X = int(input())
ROTATION = 360

K = 1
while K * X % 360 != 0:
    K += 1

print(K)
