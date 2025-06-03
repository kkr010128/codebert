import math
n = int(input())

# 1以外のNの約数
divisors = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        divisors.append(i)
        if i ** 2 != n:
            divisors.append(n // i)
divisors.sort()

candidates = set()
for k in divisors[1:]:
    tmp = n
    while True:
        if tmp % k != 0:
            break
        tmp = tmp // k
    if (tmp - 1) % k == 0:
        candidates.add(k)

# N-1の約数
divisors = []
for i in range(1, int(math.sqrt(n-1)) + 1):
    if (n-1) % i == 0:
        divisors.append(i)
        if i ** 2 != n-1:
            divisors.append((n-1) // i)

for k in divisors[1:]:
    candidates.add(k)

print(len(candidates))
