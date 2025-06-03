from math import sqrt

N = int(input())
limit = int(sqrt(N))

res = [0] * (N + 1)
for x in range(1, limit+1):
    for y in range(1, limit+1):
        for z in range(1, limit+1):
            val = x * x + y * y + z * z + x * y + y * z + z * x
            if val <= N:
                res[val] += 1
            else:
                break

for i in range(1, N + 1):
    print(res[i])
