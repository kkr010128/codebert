from math import sqrt

N = int(input())
result = [0] * N

n = int(sqrt(N))

for x in range(1, n+1):
    for y in range(1, n+1):
        for z in range(1, n+1):
            check = x**2 + y**2 + z**2 + x * y + y * z + z * x

            if check <= N:
                result[check-1] += 1

for i in result:
    print(i)
