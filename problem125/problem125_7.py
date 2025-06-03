X = int(input())

K = 1
d = X
while d % 360 != 0:
    d += X
    K += 1
print(K)
