num = int(input())

k = input().split()

for i in range(len(k)):
    k[i] = int(k[i])

k.sort()

mul = 1

for i in range(num):
    mul *= int(k[i])
    if mul > 10**18:
        break

if mul > 10**18:
    print(-1)

else:
    print(mul)