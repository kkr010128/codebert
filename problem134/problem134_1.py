import sys

N = int(input())
p = list(map(int, input().split()))


for i in range(N):
    if p[i] == 0:
        print(0)
        sys.exit()

product = 1
for i in range(N):
    product = product * p[i]
    if product > 10 ** 18:
        print(-1)
        sys.exit()
        break

print(product)