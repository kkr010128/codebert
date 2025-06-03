import array

K = int(input())
s = 0

cache = [1] * K


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for i in range(1, K+1):
    cache[i-1] = [1] * K
    for j in range(i, K+1):
        cache[i-1][j-1] = array.array('i', [1] * K)
        for k in range(j, K+1):
            cache[i-1][j-1][k-1] = gcd(k, gcd(j, i))

for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            a, b, c = sorted([i, j, k])
            s += cache[a-1][b-1][c-1]

print(s)
