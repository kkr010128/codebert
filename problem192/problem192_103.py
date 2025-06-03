n = int(input())
a = list(map(int, input().split()))
l = (2 * 10 ** 5) + 1
b = [0] * l


def nC2(n):
    return n * (n - 1) // 2


for i in range(n):
    b[a[i]] += 1

ttl = 0
for j in range(l):
    ttl += b[j] * (b[j] - 1) // 2

for k in range(n):
    print(ttl - nC2(b[a[k]]) + nC2(b[a[k]] - 1))
